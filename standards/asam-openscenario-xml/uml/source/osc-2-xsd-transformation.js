!INC Local Scripts.EAConstants-JScript

//
// This Script transforms OpenSCENARIO into an XSD File
// =================================================================================
//


function Main(filename)
{
	try {
		var fso = new ActiveXObject("Scripting.FileSystemObject");
		
		// Show the script output window
		Repository.EnsureOutputVisible( "Script" );
		
		// Get the currently selected package in the Project Browser
		var asamPackage as EA.Package;
		var currentPackage as EA.Package;
		// getr the ASAM package
		asamPackage = Repository.Models.GetAt(0);
		for (var i =0; i< asamPackage.Packages.Count ;i++)
		{
			if (asamPackage.Packages.GetAt(i).Name == "OpenSCENARIO")
			{
				currentPackage = asamPackage.Packages.GetAt(i);
				break;
			}
		}
		
		if ( currentPackage)
		{
		    if (filename==null) filename = Repository.GetProjectInterface().GetFileNameDialog ("", "Schema Files|*.xsd", 1, 0 ,"", 0)
			var file = fso.CreateTextFile(filename, true);
			WriteHeader(file, 1);
			ProcessPackage(file, currentPackage);
			file.WriteLine("</xsd:schema>");
			file.Close();
		}else
		{
			throw "Select a <XSDschema> Package to create the Schema";
		}
		
		
	} catch(exception)
	{
		if  (typeof exception =="string")
		{
			Session.Output( "Error: " + exception );
		}
		else
		{
			throw exception;
		}
	}
	Session.Output("XSD Transformation done")
}


function ProcessPackage( file, currentPackage )
{
	if ( currentPackage )
		{
			var packageElements as EA.Collection;
			packageElements = currentPackage.Elements;
			for ( var i = 0 ; i < packageElements.Count ; i++ )
			{
				// Get the current element
				var currentElement as EA.Element;
				currentElement = packageElements.GetAt( i );
				if ( currentElement.Type == "Class" )
				{
					if (HasStereotype(currentElement,"XSDcomplexType"))
					{
						ProcessComplexType(file, currentElement, 1);
					} else if (HasStereotype(currentElement,"XSDgroup"))
					{
						ProcessGroup(file, currentElement, 1);
					}else if (HasStereotype(currentElement,"enumeration"))
					{
						ProcessEnumeration(file, currentElement, 1);
					}else if (HasStereotype(currentElement,"XSDsimpleContent"))
					{
						ProcessSimpleContent(file, currentElement, 1);
					}
					
					if (HasStereotype(currentElement,"XSDtopLevelElement"))
					{
						ProcessTopLevelElement(file, currentElement, 1);
					}
					
				} else if (currentElement.Type == "PrimitiveType")
				{
					ProcessPrimitiveType(file, currentElement, 1);
				}
			}
			var subPackages as EA.Collection;
			subPackages = currentPackage.Packages;
			var packages = [];
			for ( var i = 0 ; i < subPackages.Count ; i++ )
			{
				packages.push(subPackages.GetAt( i ));
			}
			packages.sort(PackageSort);
			for ( var i = 0 ; i < packages.length ; i++ )
			{
				ProcessPackage(file, packages[i]);
			}
		}

}

function PackageSort(a, b){
		var order = ["PrimitiveTypes","Enums", "Classes"];
		for ( var i = 0 ; i < order.length ; i++ )
		{
			if (a.Name == order[i])
			{
				return -1;
			}else if (b.Name == order[i])
			{
				return 1;
			}
		}
		return 0;
};

function ProcessTopLevelElement(file, modelClass, indent)
{
	file.WriteLine(MakeIndent(indent) +"<xsd:element name=\""+GetTaggedValue(modelClass, "elementName")+"\" type=\""+modelClass.Name+"\"/>");
}


function WriteHeader(file, indent)
{
	
	file.WriteLine("<?xml version=\"1.0\" encoding=\"utf-8\"?>");
	file.WriteLine("<xsd:schema xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">");
	file.WriteLine("<!--");
	file.WriteLine("ASAM OpenSCENARIO XML V1.4.0");
	file.WriteLine("");
	file.WriteLine("__(c)__ by ASAM e.V., 2026");
	file.WriteLine("");
	file.WriteLine("Description of dynamic content in driving simulations");
	file.WriteLine("");
	file.WriteLine("Any use is limited to the scope described in the ASAM license terms. ");
	file.WriteLine("In alteration to the regular license terms, ASAM allows unrestricted distribution of this standard.");
	file.WriteLine("Paragraph 2 (1) of ASAM's regular license terms is therefore substituted by the following clause:");
	file.WriteLine("\"The licensor grants everyone a basic, non-exclusive and unlimited license to use the standard ASAM OpenSCENARIO XML\".");
	file.WriteLine("See www.asam.net/license.html for further details.");
	file.WriteLine("-->");
	file.WriteLine(MakeIndent(indent) +"<xsd:element name=\"OpenSCENARIO\" type=\"OpenScenario\"/>");
	file.WriteLine(MakeIndent(indent) +"<xsd:simpleType name=\"parameter\">");
	file.WriteLine(MakeIndent(indent+1) +"<xsd:restriction base=\"xsd:string\">");
	file.WriteLine(MakeIndent(indent+2) +"<xsd:pattern value=\"[$][A-Za-z_][A-Za-z0-9_]*\"/>");
	file.WriteLine(MakeIndent(indent+1) +"</xsd:restriction>");
	file.WriteLine(MakeIndent(indent) +"</xsd:simpleType>");
	file.WriteLine(MakeIndent(indent) +"<xsd:simpleType name=\"expression\">");
	file.WriteLine(MakeIndent(indent+1) +"<xsd:restriction base=\"xsd:string\">");
	file.WriteLine(MakeIndent(indent+2) +"<xsd:pattern value=\"[$][\{][ A-Za-z0-9_\\+\\-\\*/%$\\(\\)\\.,]*[\\}]\"/>");
	file.WriteLine(MakeIndent(indent+1) +"</xsd:restriction>");
	file.WriteLine(MakeIndent(indent) +"</xsd:simpleType>");
	
}

function ProcessPrimitiveType(file, primitiveType, indent)
{
	var name = primitiveType.Name ;
	
	if (name == "int" || name == "unsignedInt" || name == "boolean" || name == "double" || name == "unsignedShort")
	{
		file.WriteLine(MakeIndent(indent) +"<xsd:simpleType name=\""+ToFirstUpper(primitiveType.Name)+"\">");
		file.WriteLine(MakeIndent(indent+1) +"<xsd:union memberTypes=\"expression parameter xsd:"+primitiveType.Name+"\"/>");
		file.WriteLine(MakeIndent(indent) +"</xsd:simpleType>");
		
	} else if (name == "string" || name == "dateTime")
	{
		file.WriteLine(MakeIndent(indent) +"<xsd:simpleType name=\""+ToFirstUpper(primitiveType.Name)+"\">");
		file.WriteLine(MakeIndent(indent+1) +"<xsd:union memberTypes=\"parameter xsd:"+primitiveType.Name+"\"/>");
		file.WriteLine(MakeIndent(indent) +"</xsd:simpleType>");
	}else if (name == "id")
	{
		file.WriteLine(MakeIndent(indent) +"<xsd:attributeGroup name=\"Identifier\">");
		file.WriteLine(MakeIndent(indent+1) +"<xsd:attribute name=\"name\" type=\"xsd:string\"/>");
		file.WriteLine(MakeIndent(indent) +"</xsd:attributeGroup>");

	}else
	{
		Session.Output("Unknown primitve type" +primitiveType.Name)
	}

}
function ProcessComplexType(file, modelClass,indent)
{
	var className = modelClass.Name;
	file.WriteLine(MakeIndent(indent) +"<xsd:complexType name=\""+className+"\">");
	if (HasStereotype(modelClass, "deprecated"))
	{
		file.WriteLine(MakeIndent(indent+1) + GetDeprecatedString(modelClass));
	}
	ProcessType(file, modelClass,indent+1);
	file.WriteLine(MakeIndent(indent) +"</xsd:complexType>");
	var xsdWrapperType = GetTaggedValue(modelClass, "xsdWrapperType");
	if (xsdWrapperType != null)
	{
			ProcessWrapperType(file, xsdWrapperType, className, GetTaggedValue(modelClass, "xsdWrapperElementName"),indent+1);
	}

}

function GetDeprecatedString(modelClass)
{
	/*
	var attributes as EA.Collection;
	attributes = modelClass.Attributes;
	
	var attributeNames = "";
	for(var i=0;i<attributes.Count;i++)
		{
			var a as EA.Attribute;
			a = attributes.GetAt(i);
			attributeNames += a.Name + ", ";
	}
	
	return "<xsd:annotation><xsd:appinfo>deprecated</xsd:appinfo><xsd:documentation lang=\"en\">"+attributeNames+"</xsd:documentation></xsd:annotation>";*/
	return "<xsd:annotation><xsd:appinfo>deprecated</xsd:appinfo></xsd:annotation>";
}
function ProcessSimpleContent(file, modelClass,indent)
{
	var className = modelClass.Name;
	var umlPropertyName = GetTaggedValue(modelClass, "umlPropertyName");
	var xsdType = GetTaggedValue(modelClass, "xsdType");
	var attributes as EA.Collection;
	attributes = modelClass.Attributes;
	
	file.WriteLine(MakeIndent(indent) +"<xsd:complexType name=\""+className+"\">");
	if (HasStereotype(modelClass, "deprecated"))
	{
		file.WriteLine(MakeIndent(indent+1) + GetDeprecatedString(modelClass));
	}
	file.WriteLine(MakeIndent(indent+1) +"<xsd:simpleContent>");
	file.WriteLine(MakeIndent(indent+2) +"<xsd:extension base=\"xsd:"+xsdType+"\">");

	for ( var i = 0 ; i < attributes.Count ; i++ )
	{
		var attribute as EA.Attribute;
		attribute = attributes.GetAt(i);
		
		if (attribute.Name != umlPropertyName)
		{
			ProcessAttribute(file, attributes.GetAt(i), modelClass, indent+1);			
		}
	}	
	file.WriteLine(MakeIndent(indent+2) +"</xsd:extension>");
	file.WriteLine(MakeIndent(indent+1) +"</xsd:simpleContent>");
	file.WriteLine(MakeIndent(indent) +"</xsd:complexType>");
	var xsdWrapperType = GetTaggedValue(modelClass, "xsdWrapperType");
	if (xsdWrapperType != null)
	{
			ProcessWrapperType(file, xsdWrapperType, className, GetTaggedValue(modelClass, "xsdWrapperElementName"), indent);
	}

}

function ProcessEnumeration(file, modelClass,indent)
{
	var enumerationClass as EA.Element;
	enumerationClass = modelClass;

	file.WriteLine(MakeIndent(indent) +"<xsd:simpleType name=\""+enumerationClass.Name+"\">");
	if (HasStereotype(modelClass, "deprecated"))
	{
		file.WriteLine(MakeIndent(indent+1) + GetDeprecatedString(modelClass));
	}
	file.WriteLine(MakeIndent(indent+1) +"<xsd:union>");
	file.WriteLine(MakeIndent(indent+2) +"<xsd:simpleType>");
	file.WriteLine(MakeIndent(indent+3) +"<xsd:restriction base=\"xsd:string\">");
	var enumerationValues as EA.Collection;
	enumerationValues = enumerationClass.Attributes;
	for ( var i = 0 ; i < enumerationValues.Count ; i++ )
	{
		var isDeprecated = HasStereotype(enumerationValues.GetAt(i), "deprecated");
		if (!isDeprecated)
		{
			file.WriteLine(MakeIndent(indent+4) +"<xsd:enumeration value=\""+enumerationValues.GetAt(i).Name+"\"/>");
		} else {
			file.WriteLine(MakeIndent(indent+4) +"<xsd:enumeration value=\""+enumerationValues.GetAt(i).Name+"\">");
			file.WriteLine(MakeIndent(indent+5)+ GetDeprecatedString(modelClass));
			file.WriteLine(MakeIndent(indent+4) +"</xsd:enumeration>");
		}
	}
	file.WriteLine(MakeIndent(indent+3) +"</xsd:restriction>");
	file.WriteLine(MakeIndent(indent+2) +"</xsd:simpleType>");
	file.WriteLine(MakeIndent(indent+2) +"<xsd:simpleType>");
	file.WriteLine(MakeIndent(indent+3) +"<xsd:restriction base=\"parameter\"/>");
	file.WriteLine(MakeIndent(indent+2) +"</xsd:simpleType>");
	file.WriteLine(MakeIndent(indent+1) +"</xsd:union>");
	file.WriteLine(MakeIndent(indent) +"</xsd:simpleType>");
}

function ProcessGroup(file, modelClass,indent)
{
	file.WriteLine(MakeIndent(indent) +"<xsd:group name=\""+modelClass.Name+"\">");
	if (HasStereotype(modelClass, "deprecated"))
	{
		file.WriteLine(MakeIndent(2) + GetDeprecatedString(modelClass));
	}
	ProcessType(file, modelClass,indent+1);
	file.WriteLine(MakeIndent(indent) +"</xsd:group>");

}

function ProcessType(file, modelClass, indent)
{
	var connectors = GetConnectors(modelClass);
	var elements = connectors["Elements"];
	var nameRefs = connectors["NameRefs"];
	
	var modelGroupResults = GetModelGroup(modelClass);
	if (elements.length > 0)
	{
		file.WriteLine(MakeIndent(indent) +"<xsd:"+modelGroupResults['fullResult']+">");
		for ( var i = 0 ; i < elements.length ; i++ )
		{
			ProcessElement(file, elements[i], modelClass, indent+1);
		}
		file.WriteLine(MakeIndent(indent) +"</xsd:"+modelGroupResults['modelGroup']+">");
	}
	for ( var i = 0 ; i < nameRefs.length ; i++ )
	{
		ProcessNameRef(file, nameRefs[i], modelClass.Name, indent);
	}
	var attributes as EA.Collection;
	attributes = modelClass.Attributes;
	for ( var i = 0 ; i < attributes.Count ; i++ )
	{
		ProcessAttribute(file, attributes.GetAt(i), modelClass, indent);
	}

}
function ProcessElement(file, modelElement, modelClass, indent)
{
	var connector as EA.Connector;
	connector = modelElement["Connector"];
	// Multiplicity
	var minOccurs = "";
	var maxOccurs = "";
	var multiplicity = connector.SupplierEnd.Cardinality;
	
	var lowerUpper = GetLowerUpper(multiplicity);
	// Get the supplierEndClass
	var supplierEndClass = Repository.GetElementByID(connector.SupplierID);
	
	if (lowerUpper == null)
	{
		throw "Cardinality of property '"+connector.SupplierEnd.Role+"' of '" + modelClass.Name +"' must be in the format '0..1', '1..*', '0..2', '1..1'"
	}
	
	if (lowerUpper["Lower"] != "1")
	{
		minOccurs = " minOccurs=\""+ lowerUpper["Lower"] + "\"";
	}
	var xsdWrapperType = GetTaggedValue(supplierEndClass, "xsdWrapperType");
	
	var type = supplierEndClass.Name
	
	if (xsdWrapperType != null && HasStereotype(connector, "XSDwrapped"))
	{
		// if wrapped maxOccurs is always 1 (empty)
		type = xsdWrapperType;
		
	}else if (lowerUpper["Upper"] != "1")
	{
		if (lowerUpper["Upper"] == "*")
		{
			maxOccurs = " maxOccurs=\"unbounded\"";
		}
		else
		{
			minOccurs = " maxOccurs=\""+ lowerUpper["Lower"] + "\"";
		}
	}
	
	var isDeprecated = HasStereotype(connector, "deprecated");
	
	// Process Connector
	if (HasStereotype(supplierEndClass,"XSDgroup"))
	{
		
		if (!isDeprecated)
		{
			file.WriteLine(MakeIndent(indent) +"<xsd:group ref=\""+supplierEndClass.Name+"\"" +minOccurs + maxOccurs +"/>");
			
		}else
		{
			file.WriteLine(MakeIndent(indent) +"<xsd:group ref=\""+supplierEndClass.Name+"\"" +minOccurs + maxOccurs +"/>");
			file.WriteLine(MakeIndent(indent+1) + GetDeprecatedString(modelClass));
			file.WriteLine(MakeIndent(indent) +"</xsd:group>");
			
		}
	}else{
		var elementName = GetElementName(connector.SupplierEnd.Role, connector);
		if (!isDeprecated)
		{
			file.WriteLine(MakeIndent(indent) +"<xsd:element name=\""+elementName +"\" type=\"" + type + "\"" +minOccurs + maxOccurs +"/>");
			
		}else
		{
			file.WriteLine(MakeIndent(indent) +"<xsd:element name=\""+elementName +"\" type=\"" + type + "\"" +minOccurs + maxOccurs +">");
			file.WriteLine(MakeIndent(indent+1) + GetDeprecatedString(modelClass));
			file.WriteLine(MakeIndent(indent) +"</xsd:element>");
			
		}
	}
	

}

function ProcessWrapperType(file, xsdWrapperType, wrappedClassName, xsdWrapperElementName, indent)
{    
	file.WriteLine(MakeIndent(indent) +"<xsd:complexType name=\""+xsdWrapperType+"\">");
	file.WriteLine(MakeIndent(indent+1) +"<xsd:sequence>");
	file.WriteLine(MakeIndent(indent+2) +"<xsd:element name=\""+xsdWrapperElementName+"\" type=\"" +wrappedClassName+"\" minOccurs=\"0\" maxOccurs=\"unbounded\"/>");
	file.WriteLine(MakeIndent(indent+1) +"</xsd:sequence>");
	file.WriteLine(MakeIndent(indent) +"</xsd:complexType>");
}
	
function ProcessAttribute(file, modelElement, modelClass, indent)
{
	var attribute as EA.Attribute;
	attribute = modelElement;
	var isDeprecated = HasStereotype(attribute, "deprecated");
	
	var use = "";
	if (attribute.LowerBound == "1")
	{
		use = " use=\"required\"";

	}
	
	if (attribute.Type != "id")
	{
		if (!isDeprecated)
		{
			file.WriteLine(MakeIndent(indent) +"<xsd:attribute name=\""+attribute.Name+"\" type=\""+ToFirstUpper(attribute.Type)+"\""+use+"/>");
					
		}else
		{
			file.WriteLine(MakeIndent(indent) +"<xsd:attribute name=\""+attribute.Name+"\" type=\""+ToFirstUpper(attribute.Type)+"\""+use+">");
			file.WriteLine(MakeIndent(indent+1) + GetDeprecatedString(modelClass));
			file.WriteLine(MakeIndent(indent) +"</xsd:attribute>");
			
		}
	} else
	{
		if (!isDeprecated)
		{
			file.WriteLine(MakeIndent(indent) +"<xsd:attributeGroup ref=\"Identifier\"/>");
					
		}else
		{
			file.WriteLine(MakeIndent(indent) +"<xsd:attributeGroup ref=\"Identifier\">");
			file.WriteLine(MakeIndent(indent+1) + GetDeprecatedString(modelClass));
			file.WriteLine(MakeIndent(indent) +"</xsd:attribute>");
			
		}
	
	}
	
}

function ProcessNameRef(file, connector, modelClassName, indent)
{
	var multiplicity = connector.SupplierEnd.Cardinality;
	var name = connector.SupplierEnd.Role;
						
	var lowerUpper = GetLowerUpper(multiplicity);
	
	var use = "";
	var xsdType = GetTaggedValue(connector,"xsdType");
	if (lowerUpper["Lower"] != "0")
	{
		use = " use=\"required\"";

	}
	var isDeprecated = HasStereotype(connector, "deprecated");
	if (!isDeprecated)
	{
		file.WriteLine(MakeIndent(indent) +"<xsd:attribute name=\""+name+"\" type=\""+ToFirstUpper(xsdType)+"\""+use+"/>");
	} else
	{
		file.WriteLine(MakeIndent(indent) +"<xsd:attribute name=\""+name+"\" type=\""+ToFirstUpper(xsdType)+"\""+use+">");
		file.WriteLine(MakeIndent(indent+1) + GetDeprecatedString(modelClassName));
		file.WriteLine(MakeIndent(indent) +"</xsd:attribute>");
	}
	
}

function GetConnectors(modelElement)
{
	var modelClass as EA.Element;
	modelClass = modelElement;
	var connectors as EA.Collection;
	connectors = modelClass.Connectors;
	
	var result = {};
	var elements = [];
	var nameRefs = [];
	result["Elements"] = elements;
	result["NameRefs"] = nameRefs;
	
	for ( var i = 0 ; i < connectors.Count ; i++ )
	{
		var connector as EA.Connector;
		connector = connectors.GetAt(i);
		// filter out the nameRef and the outgoing
		if (connector.clientId == modelClass.ElementID && connector.Type == "Association" && (connector.SupplierEnd.Role == null || connector.SupplierEnd.Role == ""))
		{
			throw "Every property of class '"+ modelClass.Name +"' must define a name at association end role";
		}
		if (connector.clientId == modelClass.ElementID && connector.Type == "Association"  && !HasStereotype(connector,"nameRef") &&  connector.Stereotype !="transient"){			
			var arrayElement = {};
			arrayElement["Connector"] = connector;
			arrayElement["Position"] = GetPosition(connector);
			
			
			elements.push(arrayElement);
		}else if (HasStereotype(connector,"nameRef") && connector.clientId == modelClass.ElementID)
		{
			nameRefs.push(connector);
		}
	};
	
	
	
	elements.sort(function(a, b){
		if (a["Position"] < b["Position"]) {
			return -1;
		}
		if (a["Position"] > b["Position"]) {
			return 1;
		}
		return 0;
	});
		
	
	return result;
	
	
}

function GetPosition(connector)
{
	if (connector.TaggedValues != null){
		var tag = connector.TaggedValues.GetByName("position");
		if (tag != null)
		{
			
			return parseInt(tag.Value);
		}
	}
	return -1;
}

function GetLowerUpper(umlCardinality)
{
	var result = {};
	var regEx = /(\d+)\.\.([\d+|\*])/;
	var matchResult = umlCardinality.match(regEx);
	if( matchResult != null)
	{
		result["Lower"] = matchResult[1];
		result["Upper"] = matchResult[2];
		return result;
	}
	return null;
	
}
function GetOccurrence(umlClass)
{
	var results = {};
	results['minOccurs'] = GetTaggedValue(umlClass,"minOccurs") ? GetTaggedValue(umlClass,"minOccurs") : 1;
	results['maxOccurs'] = GetTaggedValue(umlClass,"maxOccurs") ? GetTaggedValue(umlClass,"maxOccurs") : 1
	return results;
	
}
function GetModelGroup(umlClass)
{
	var taggedValue = GetTaggedValue(umlClass,"modelGroup");
	var occurs = GetOccurrence(umlClass);
	var modelGroup = taggedValue == null || taggedValue == "" ? "sequence" : taggedValue;
	var fullResult = modelGroup;
	if (occurs['minOccurs'] && occurs['minOccurs'] != 1) {
		fullResult = modelGroup + " minOccurs=\"" + occurs['minOccurs'] + "\"";
	}
	if (occurs['maxOccurs'] && occurs['maxOccurs'] != 1) {
		occurs['maxOccurs'] = occurs['maxOccurs'] == "*" ? "unbound" : occurs['maxOccurs'];
		fullResult = modelGroup + " maxOccurs=\"" + occurs['maxOccurs'] + "\"";
	}
	return {"modelGroup": modelGroup, "fullResult": fullResult};
}
function ToFirstUpper(propertyName)
{
	return propertyName.substring(0,1).toUpperCase() + propertyName.substring(1);
}

function GetElementName(propertyName, connector)
{
	
	var xsdElementName = GetTaggedValue(connector,"xsdElementName");
	if (xsdElementName == null)
	{
		xsdElementName = ToFirstUpper(propertyName);
	}
	return xsdElementName;
}

function GetTaggedValue(modelElement, key)
{
	for (var i =0; i< modelElement.TaggedValues.Count ;i++)
	{
		if (modelElement.TaggedValues.GetAt(i).Name == key)
		{
			return modelElement.TaggedValues.GetAt(i).Value;
		}
	}
	return null;
}

String.prototype.trim = function()
{
    return this.replace(/^\s+|\s+$/g, '');
};
	
function HasStereotype(modelElement, stereotypeName)
{
	if (modelElement.Stereotype == stereotypeName)
		return true;
	var stereotypes = modelElement.StereotypeEx;
	var list = stereotypes.split(",");
	for (var i = 0; i< list.length;i++)
	{

		if (list[i].trim() == stereotypeName)
		{
			return true;
		}
	}
	return false;
}

function MakeIndent( counter )
{
	return Array(counter+1).join("\t")
}
Main();