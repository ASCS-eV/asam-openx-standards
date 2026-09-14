# Setting up a machine to run the pipeline

[`README.md`](README.md) says *what* the pipeline produces and *why*; this file is how to get a
machine that can actually run it. Everything here was established by doing it from scratch, and
every trap in [Things that will bite you](#things-that-will-bite-you) is one that actually did.

If you only want to *consume* the generated OWL and SHACL, you need none of this — read
`standards/*/generated/` and stop here.

## What you need, and why the versions are exact

| Component | Required | Why not "any recent version" |
|---|---|---|
| JDK | **Temurin 21.0.12+8** | `toolchain-lock.json` records `build_inputs` fingerprints of the *compiled* ShapeChange runtime. The same source compiled by 21.0.11 and 21.0.12 produces different fingerprints. A different JDK is not wrong, but it invalidates the recorded values, so it must be a deliberate `build_environment` change. |
| Maven | **3.9.9** | Same reason. The lock publishes the official SHA-512 of both published archives, so the download verifies itself. |
| Python | 3.12+ | Runs the pipeline scripts. |
| Python packages | exactly `scripts/requirements.txt` | rdflib performs the final serialization, so a minor bump changes artifact bytes. |
| Enterprise Architect | only for a **re-export** | Not needed to generate OWL/SHACL/XSD. The `.scxml` exports are committed precisely so nobody else needs EA. |

The pinned values live in [`toolchain-lock.json`](toolchain-lock.json) under `build_environment`.
**That file is the source of truth; if it disagrees with this one, it wins.**

## Layout

The three generators are **siblings of the repository**, never nested inside it:

```
<parent>/
├── asam-openx-standards/   ← this repository
├── ShapeChange/            ← github.com/ASCS-eV/ShapeChange
├── shacl-play/             ← github.com/ASCS-eV/shacl-play
├── owl2shacl/              ← github.com/ASCS-eV/owl2shacl
└── .toolchain/             ← JDK + Maven (suggested; anywhere outside the repos is fine)
```

> **Trap:** if you are working in the copy of this repository that sits inside another project as
> a **git submodule** (`.../submodules/asam-openx-standards/`), its `..` is that project's
> `submodules/` directory, *not* the parent holding `ShapeChange/`. Either pass absolute paths to
> `--shapechange`/`--shaclplay`/`--rules`, or use a standalone clone at the correct level. A
> submodule checkout is fine for editing; it is the wrong place to assume `../ShapeChange` resolves.

## 1. Install the JDK and Maven (portable, no admin)

Nothing needs to go on the system `PATH` or into the registry — extract both and point at them.

**Maven**, verified against the lock's own checksum:

```powershell
$tools = "C:\repository\.toolchain"; New-Item -ItemType Directory -Force $tools | Out-Null
curl.exe -sSL -o "$tools\apache-maven-3.9.9-bin.zip" `
  "https://archive.apache.org/dist/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.zip"

# The expected value is in toolchain-lock.json -> build_environment.maven_archive_sha512,
# keyed by archive filename. Compare before extracting.
(Get-FileHash "$tools\apache-maven-3.9.9-bin.zip" -Algorithm SHA512).Hash.ToLower()

Expand-Archive "$tools\apache-maven-3.9.9-bin.zip" -DestinationPath $tools
```

**JDK** — Temurin 21.0.12+8 from the Adoptium API:

```powershell
curl.exe -sSL --retry 5 --retry-all-errors --http1.1 -o "$tools\temurin-21.zip" `
  "https://api.adoptium.net/v3/binary/version/jdk-21.0.12%2B8/windows/x64/jdk/hotspot/normal/eclipse?project=jdk"
Expand-Archive "$tools\temurin-21.zip" -DestinationPath $tools
```

> The Adoptium CDN frequently drops the connection part-way through this ~205 MB download, and
> `curl` reports a truncated transfer. **Always verify the archive opens before extracting it** —
> a truncated zip fails with *"End of Central Directory record could not be found"*. Use
> `--retry 5 --retry-all-errors --http1.1` and re-download if it fails.

Verify both report exactly what the lock requires:

```powershell
$env:JAVA_HOME = "$tools\jdk-21.0.12+8"
& "$env:JAVA_HOME\bin\java.exe" -version          # Temurin-21.0.12+8
& "$tools\apache-maven-3.9.9\bin\mvn.cmd" -v      # Apache Maven 3.9.9, vendor Eclipse Adoptium
```

On Linux/WSL the same applies with the `.tar.gz` archives; use the `.tar.gz` checksum from the
lock. Note that a distro-packaged JDK is usually the wrong patch level — Ubuntu 26.04 ships
JDK 25, which is not what the lock pins.

## 2. Clone the generators at their locked commits

Read the commits from `toolchain-lock.json` → `tools.*.commit`. Check out the **commit**, not the
branch tip: the branch is where work happens, the lock is what a run is validated against.

```powershell
git clone https://github.com/ASCS-eV/ShapeChange.git
git clone https://github.com/ASCS-eV/shacl-play.git
git clone https://github.com/ASCS-eV/owl2shacl.git

git -C ShapeChange checkout <tools.shapechange.commit>
git -C shacl-play  checkout <tools.shacl_play.commit>
git -C owl2shacl   checkout <tools.owl2shacl.commit>
```

`generate_semantic_artifacts.py` refuses to build unless each checkout is **clean**, at the
**exact** locked commit, with the locked `upstream_base` as an ancestor and a carried-commit list
matching the lock exactly. That check is the point — do not work around it.

## 3. Python environment

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r scripts\requirements.txt
```

## 4. Run it

```powershell
$tools = "C:\repository\.toolchain"
$env:JAVA_HOME = "$tools\jdk-21.0.12+8"
$env:PATH      = "$tools\jdk-21.0.12+8\bin;$env:PATH"   # required — see the traps below

foreach ($standard in "asam-opendrive", "asam-openscenario-xml") {
  .\.venv\Scripts\python.exe scripts\generate_semantic_artifacts.py `
      --standard $standard `
      --shapechange ..\ShapeChange `
      --shaclplay ..\shacl-play `
      --rules ..\owl2shacl\owl2sh-closed.ttl `
      --mvn "$tools\apache-maven-3.9.9\bin\mvn.cmd"
}
```

`--mvn` exists so Maven need not be on `PATH`. `--shaclplay` is a **checkout root, not a jar**:
the jar is always rebuilt from the locked source, so the binary that runs is provably the one the
lock describes.

Expect a first run to take a while: it builds ShapeChange and shacl-play from source, and the
canonicalization step is superlinear in blank nodes.

## Things that will bite you

### Maven caches *failures*, and will not retry them

A transient network failure writes a `*.lastUpdated` marker into `~/.m2/repository`, and Maven
then refuses to retry that artifact for the rest of the update interval — so the build keeps
failing with the original error long after the network recovered. Both `jitpack.io` **and Maven
Central** have been observed timing out on a corporate network within a single build.

Clear the markers and retry:

```powershell
Get-ChildItem "$env:USERPROFILE\.m2\repository" -Recurse -Filter "*.lastUpdated" |
  Remove-Item -Force
```

Before blaming the network, check the artifact is actually reachable — the marker file records
the original error and the repositories it tried, which tells you which one to test.

### shacl-play needs jitpack.io

`shacl-play-app` depends on `com.github.sparna-git.xls2rdf:xls2rdf-lib`, pinned to a **JitPack
commit build**. JitPack builds on demand, so the first request for an uncached commit can be slow
enough to time out and then succeed on retry. If jitpack.io is blocked on your network, the
shacl-play build cannot complete — there is no Maven Central fallback for this artifact.

That pin is deliberate: it is what makes the shacl-play jar's content fingerprint reproducible at
all (`sparna-git/shacl-play#347`). Do not replace it with `master-SNAPSHOT`.

### The ShapeChange build GPG-signs every artifact

`maven-gpg-plugin` (`sign-artifacts`) is in ShapeChange's main build section, not behind a
profile, so **every** `mvn install` signs. If your GPG key lives on a smartcard this adds roughly
20 seconds per signature and can appear to hang while waiting for the agent — which is invisible
when the build runs in a non-interactive shell.

`-Dgpg.skip=true` skips it. This cannot affect `shapechange_runtime_fingerprint`: that is computed
from `shapechange-core/target/classes` plus the resolved dependency jars, and `.asc` files are
neither. Confirm the fingerprint still reproduces the first time you use the flag.

### `JAVA_HOME` alone is not enough — the JDK must be first on `PATH`

`generate_semantic_artifacts.py` shells out to `java` and checks that it reports the locked
version, so a system JDK earlier on `PATH` fails the run even with `JAVA_HOME` set correctly:

```
java -version does not report the locked JDK 21.0.12+8:
openjdk version "21.0.5" ... IBM Semeru Runtime ... Eclipse OpenJ9 VM
```

That check is doing its job — the fingerprints depend on the compiler. Set both:

```powershell
$env:JAVA_HOME = "$tools\jdk-21.0.12+8"
$env:PATH      = "$tools\jdk-21.0.12+8\bin;$env:PATH"
```

### Maven ignores `HTTP_PROXY` / `HTTPS_PROXY`

This is the single most confusing failure here, because every other tool works. Java does not
read those environment variables, so on a network where a local proxy is mandatory Maven
connects directly and times out — while `curl` and PowerShell fetch the identical URL happily.
The symptom is a `Connect timed out` for a host you just proved is reachable.

Fix it once, in `~/.m2/settings.xml`:

```xml
<settings>
  <proxies>
    <proxy>
      <id>corp-https</id><active>true</active><protocol>https</protocol>
      <host>localhost</host><port>3128</port>
      <nonProxyHosts>localhost|127.0.0.1|*.internal.example</nonProxyHosts>
    </proxy>
    <!-- repeat with <protocol>http</protocol> -->
  </proxies>
</settings>
```

Read the host and port from `HTTPS_PROXY`. `MAVEN_OPTS="-Dhttps.proxyHost=… -Dhttps.proxyPort=…"`
also works but is easy to mangle: PowerShell and `cmd.exe` both split `-D` arguments containing
`.` or `|`, producing errors like *"Unknown lifecycle phase `.skip=true`"* or
*"Der Befehl 127.0.0.1 ist entweder falsch geschrieben…"*. The settings file avoids all of it.

### The shacl-play jar fingerprint may not reproduce, and it is not your fault

`shacl-play-app` bundles `xls2rdf-lib` from JitPack. JitPack **builds artifacts on demand**, and
Maven writes a build timestamp into the jar it produces:

```
META-INF/maven/fr.sparna.rdf.xls2rdf/xls2rdf-lib/pom.properties
  #Generated by Maven
  #Thu Aug 06 04:58:39 UTC 2026     <-- here
  version=4.0.2
```

Two JitPack builds of the *same commit* therefore differ in content, which propagates into the
onejar and changes `build_inputs.shacl_play_jar_fingerprint`. Observed directly: the two cached
coordinate forms of commit `ac18090cfd` have different SHA-256 despite identical length.

If the run stops with

```
shacl-play jar content fingerprint <x> does not match the locked
build_inputs.shacl_play_jar_fingerprint (<y>)
```

**do not simply overwrite the locked value.** That is the check working. Establish first whether
the difference is the JitPack timestamp or something real — unzip both jars and compare
`pom.properties` — and record the finding rather than silencing it.

### A background shell hides interactive prompts

Both of the above can block on something that wants input. If a run produces no output for many
minutes, check whether the process is actually working:

```powershell
Get-Process java | Select-Object Id, StartTime, CPU
```

Low CPU time against a long elapsed time means it is **waiting**, not computing.

## Re-exporting a model from Enterprise Architect

Only needed to produce a new `.scxml`; see the "deliberately deferred to the next re-export"
sections in `standards/*/uml/README.md` and the batched changes tracked in the issue list.

EA is Windows-only and licensed. `eaapi.jar` is not on Maven Central — it ships with the EA
installation and must be installed into your local repository once:

```powershell
& "$tools\apache-maven-3.9.9\bin\mvn.cmd" install:install-file `
  -Dfile="C:\Program Files\Sparx Systems\EA\Java API\eaapi.jar" `
  -DgroupId=org.sparx -DartifactId=eaapi -Dversion=<your EA version> -Dpackaging=jar
```

Build ShapeChange **without** `-DskipEa` (the `ea` profile is active by default), then run the
export with `-Djava.library.path` pointing at the EA installation, because the native EA↔Java
bridge (`SSJavaCOM64.dll`) lives there rather than in ShapeChange's distribution:

```powershell
java -Djava.library.path="C:\Program Files\Sparx Systems\EA\Java API" `
     -jar ShapeChange-4.1.0-SNAPSHOT.jar -c export-model-to-scxml.config.xml `
     -x '$inputFile$' "C:\path\to\ASAM_OpenDRIVE.qeax"
```

The full procedure, including which configuration parameters are deliberately unset, is in each
model's `standards/*/uml/README.md`.
