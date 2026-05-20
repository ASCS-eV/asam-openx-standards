"""
ASAM OpenX Standards Downloader

Downloads ASAM OpenX specifications from publications.pages.asam.net and converts
them to markdown for use as AI-accessible reference documents.

Usage:
    python scripts/download_asam_specs.py [--standard STANDARD] [--all]

Standards available:
    openodd, openlabel, opendrive, openscenario-dsl, osi, opencrg, openmaterial-3d, traffic-participants

Requirements:
    pip install requests beautifulsoup4 markdownify
"""

import argparse
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md
except ImportError:
    print("ERROR: Missing dependencies. Install with:")
    print("  pip install requests beautifulsoup4 markdownify")
    sys.exit(1)

# Disable SSL warnings when using --no-verify
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Global SSL verification flag (set by --no-verify CLI arg)
VERIFY_SSL = True

# Project root
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "docs" / "specs" / "references"

# Standard definitions: name -> (base_url, nav_component, version)
STANDARDS = {
    "openodd": {
        "base_url": "https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/",
        "version": "v1.0.0",
        "date": "2025-04-03",
        "output_dir": "asam-openodd",
        "license": "Unrestricted distribution (ASAM e.V.)",
    },
    "openlabel": {
        "base_url": "https://publications.pages.asam.net/standards/ASAM_OpenLABEL/ASAM_OpenLABEL/latest/specification/",
        "version": "v1.0.0",
        "date": "2024-11-28",
        "output_dir": "asam-openlabel",
        "license": "Unrestricted distribution (ASAM e.V.)",
    },
    "opendrive": {
        "base_url": "https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/",
        "version": "v1.9.0",
        "date": "2026-05-08",
        "output_dir": "asam-opendrive",
        "license": "Unrestricted distribution (ASAM e.V.)",
    },
    "openscenario-dsl": {
        "base_url": "https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/",
        "version": "v2.2.0",
        "date": "2026-03-19",
        "output_dir": "asam-openscenario-dsl",
        "license": "Unrestricted distribution (ASAM e.V.)",
    },
    "traffic-participants": {
        "base_url": "https://publications.pages.asam.net/standards/ASAM_trafficparticipants/ASAM_TrafficParticipants_Specification/v1.0.2/specification/",
        "version": "v1.0.2",
        "date": "2025-01-01",
        "output_dir": "asam-traffic-participants",
        "license": "Unrestricted distribution (ASAM e.V.)",
    },
    "openmaterial-3d": {
        "base_url": "https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/",
        "version": "latest",
        "date": "2025-01-01",
        "output_dir": "asam-openmaterial-3d",
        "license": "Unrestricted distribution (ASAM e.V.)",
    },
}

# GitHub-hosted standards (different download strategy)
GITHUB_STANDARDS = {
    "osi": {
        "repo": "OpenSimulationInterface/open-simulation-interface",
        "branch": "master",
        "docs_path": "doc",
        "version": "v3.7.0",
        "output_dir": "asam-osi",
        "license": "MPL-2.0",
    },
    "opencrg": {
        "repo": "ASAM-OpenCRG/OpenCRG",
        "branch": "master",
        "docs_path": "doc",
        "version": "v1.2",
        "output_dir": "asam-opencrg",
        "license": "Apache-2.0",
    },
}


def fetch_page(url: str, retries: int = 3, delay: float = 1.0) -> str | None:
    """Fetch a page with retries and rate limiting."""
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=30, verify=VERIFY_SSL)
            if response.status_code == 200:
                return response.text
            elif response.status_code == 404:
                print(f"  WARNING: 404 Not Found: {url}")
                return None
            else:
                print(f"  WARNING: HTTP {response.status_code}: {url}")
        except requests.RequestException as e:
            print(f"  WARNING: Error (attempt {attempt + 1}/{retries}): {e}")
        time.sleep(delay * (attempt + 1))
    return None


def extract_nav_links(html: str, base_url: str) -> list[dict]:
    """Extract navigation links from Antora-generated page."""
    soup = BeautifulSoup(html, "html.parser")
    nav = soup.find("nav", class_="nav-menu")
    if not nav:
        print("  WARNING: Could not find navigation menu")
        return []

    links = []
    for a_tag in nav.find_all("a", class_="nav-link"):
        href = a_tag.get("href", "")
        if href and not href.startswith("#") and not href.startswith("http"):
            full_url = urljoin(base_url, href)
            title = a_tag.get_text(strip=True)
            links.append({"url": full_url, "title": title, "href": href})

    return links


def html_to_markdown(html: str, url: str) -> str:
    """Convert Antora HTML page content to clean markdown."""
    soup = BeautifulSoup(html, "html.parser")

    # Find the main content area (Antora uses <article class="doc">)
    article = soup.find("article", class_="doc")
    if not article:
        # Fallback to main content div
        article = soup.find("div", class_="content")
    if not article:
        article = soup.find("main")

    if not article:
        print(f"  WARNING: Could not find content area in {url}")
        return ""

    # Remove navigation elements within the content
    for nav in article.find_all("nav", class_="pagination"):
        nav.decompose()
    for toc in article.find_all("aside", class_="toc"):
        toc.decompose()

    # Convert to markdown using markdownify
    content = md(str(article), heading_style="ATX", code_language="")

    # Clean up excessive whitespace
    content = re.sub(r"\n{4,}", "\n\n\n", content)
    content = content.strip()

    return content


def generate_filename(href: str) -> str:
    """Generate a clean filename from the page href."""
    # Remove .html extension and path components
    name = Path(urlparse(href).path).stem

    # Clean up numbered prefixes for readability
    name = name.replace("_", "-")

    # Remove redundant standard-name prefixes
    name = re.sub(r"-openodd-", "-", name)
    name = re.sub(r"-openlabel-", "-", name)
    name = re.sub(r"-opendrive-", "-", name)

    return f"{name}.md"


def download_antora_standard(standard_key: str) -> None:
    """Download a complete Antora-based ASAM standard."""
    config = STANDARDS[standard_key]
    base_url = config["base_url"]
    output_dir = OUTPUT_DIR / config["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'=' * 60}")
    print(f"Downloading ASAM {standard_key.upper()} {config['version']}")
    print(f"Source: {base_url}")
    print(f"Output: {output_dir}")
    print(f"{'=' * 60}\n")

    # Step 1: Fetch the index page and extract navigation
    print("Fetching index page...")
    index_html = fetch_page(base_url)
    if not index_html:
        print(f"ERROR: Could not fetch index page for {standard_key}")
        return

    nav_links = extract_nav_links(index_html, base_url)
    print(f"Found {len(nav_links)} pages in navigation\n")

    if not nav_links:
        print("ERROR: No navigation links found. Check the base URL.")
        return

    # Step 2: Download each page
    downloaded = 0
    skipped = 0

    for i, link in enumerate(nav_links):
        filename = generate_filename(link["href"])
        filepath = output_dir / filename

        # Skip if already downloaded
        if filepath.exists() and filepath.stat().st_size > 100:
            print(f"  [{i+1}/{len(nav_links)}] SKIP (exists): {filename}")
            skipped += 1
            continue

        print(f"  [{i+1}/{len(nav_links)}] Downloading: {link['title']}")

        page_html = fetch_page(link["url"])
        if not page_html:
            continue

        content = html_to_markdown(page_html, link["url"])
        if not content:
            continue

        # Add metadata header
        header = f"""# ASAM {standard_key.replace('-', ' ').title()} {config['version']} — {link['title']}

> **Source**: {link['url']}
> **Standard**: ASAM {standard_key.replace('-', ' ').title()} {config['version']}, {config['date']}
> **License**: {config['license']}
> **Downloaded**: {time.strftime('%Y-%m-%d')}

---

"""
        filepath.write_text(header + content, encoding="utf-8")
        downloaded += 1

        # Rate limiting: be polite to the server
        time.sleep(0.5)

    print(f"\nDone: {downloaded} downloaded, {skipped} skipped")
    print(f"Output: {output_dir}")


def download_github_standard(standard_key: str) -> None:
    """Download a GitHub-hosted standard's documentation."""
    config = GITHUB_STANDARDS[standard_key]
    output_dir = OUTPUT_DIR / config["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'=' * 60}")
    print(f"Downloading ASAM {standard_key.upper()} {config['version']} (GitHub)")
    print(f"Repo: {config['repo']}")
    print(f"Output: {output_dir}")
    print(f"{'=' * 60}\n")

    # Use GitHub API to list files in the docs directory
    api_url = f"https://api.github.com/repos/{config['repo']}/contents/{config['docs_path']}?ref={config['branch']}"
    print(f"Fetching file list from: {api_url}")

    response = requests.get(api_url, timeout=30, verify=VERIFY_SSL)
    if response.status_code != 200:
        print(f"ERROR: Could not fetch file list: HTTP {response.status_code}")
        return

    files = response.json()
    doc_files = [
        f
        for f in files
        if isinstance(f, dict) and f.get("name", "").endswith((".md", ".rst", ".adoc"))
    ]

    print(f"Found {len(doc_files)} documentation files\n")

    for i, file_info in enumerate(doc_files):
        filename = file_info["name"]
        if not filename.endswith(".md"):
            filename = Path(filename).stem + ".md"

        filepath = output_dir / filename

        if filepath.exists():
            print(f"  [{i+1}/{len(doc_files)}] SKIP (exists): {filename}")
            continue

        print(f"  [{i+1}/{len(doc_files)}] Downloading: {file_info['name']}")
        content_response = requests.get(
            file_info["download_url"], timeout=30, verify=VERIFY_SSL
        )
        if content_response.status_code == 200:
            filepath.write_text(content_response.text, encoding="utf-8")
        time.sleep(0.3)

    print(f"\nDone. Output: {output_dir}")


def create_standard_index(standard_key: str) -> None:
    """Create an INDEX.md file listing all downloaded chapters for a standard."""
    if standard_key in STANDARDS:
        config = STANDARDS[standard_key]
    else:
        config = GITHUB_STANDARDS[standard_key]

    output_dir = OUTPUT_DIR / config["output_dir"]
    if not output_dir.exists():
        return

    files = sorted(output_dir.glob("*.md"))
    files = [f for f in files if f.name != "INDEX.md"]

    if not files:
        return

    index_content = f"""# ASAM {standard_key.replace('-', ' ').title()} {config['version']} — Chapter Index

> **Version**: {config['version']}
> **License**: {config.get('license', 'See standard')}
> **Files**: {len(files)} chapters

## Chapters

| # | File | Title |
|---|------|-------|
"""
    for i, f in enumerate(files, 1):
        # Extract title from first line
        first_line = f.read_text(encoding="utf-8").split("\n")[0]
        title = first_line.lstrip("# ").strip()
        index_content += f"| {i} | [{f.name}]({f.name}) | {title} |\n"

    index_file = output_dir / "INDEX.md"
    index_file.write_text(index_content, encoding="utf-8")
    print(f"Created index: {index_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Download ASAM OpenX specifications as markdown"
    )
    parser.add_argument(
        "--standard",
        choices=list(STANDARDS.keys()) + list(GITHUB_STANDARDS.keys()),
        help="Download a specific standard",
    )
    parser.add_argument(
        "--all", action="store_true", help="Download all standards"
    )
    parser.add_argument(
        "--index-only",
        action="store_true",
        help="Only regenerate INDEX.md files for already-downloaded standards",
    )
    parser.add_argument(
        "--list", action="store_true", help="List available standards"
    )
    parser.add_argument(
        "--no-verify",
        action="store_true",
        help="Disable SSL certificate verification (for corporate proxies)",
    )

    args = parser.parse_args()

    # Set global SSL verification
    global VERIFY_SSL
    if args.no_verify:
        VERIFY_SSL = False
        print("WARNING: SSL verification disabled\n")

    if args.list:
        print("Available ASAM OpenX standards:\n")
        print(f"{'Standard':<25} {'Version':<10} {'Source':<15} {'License'}")
        print("-" * 80)
        for key, config in STANDARDS.items():
            print(
                f"{key:<25} {config['version']:<10} {'Antora':<15} {config['license']}"
            )
        for key, config in GITHUB_STANDARDS.items():
            print(
                f"{key:<25} {config['version']:<10} {'GitHub':<15} {config['license']}"
            )
        return

    if args.index_only:
        for key in list(STANDARDS.keys()) + list(GITHUB_STANDARDS.keys()):
            create_standard_index(key)
        return

    if args.all:
        for key in STANDARDS:
            download_antora_standard(key)
            create_standard_index(key)
        for key in GITHUB_STANDARDS:
            download_github_standard(key)
            create_standard_index(key)
    elif args.standard:
        if args.standard in STANDARDS:
            download_antora_standard(args.standard)
        else:
            download_github_standard(args.standard)
        create_standard_index(args.standard)
    else:
        parser.print_help()
        print("\nExample:")
        print("  python scripts/download_asam_specs.py --standard openodd")
        print("  python scripts/download_asam_specs.py --all")


if __name__ == "__main__":
    main()
