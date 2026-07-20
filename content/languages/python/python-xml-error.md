---
title: "[Solution] Python xml Module Error — Parse, DOM, and SAX Failures"
description: "Fix Python xml module errors including ElementTree parse failures, DOM tree errors, SAXParseException, and XMLSyntaxError. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 242
---

# Python xml Module Error — Parse, DOM, and SAX Failures

The `xml` package in Python provides multiple ways to process XML: `xml.etree.ElementTree` for tree-based parsing, `xml.dom` for DOM manipulation, and `xml.sax` for event-driven parsing. Errors occur when XML is malformed, namespaces are incorrect, or the parser encounters unexpected characters.

## Common Causes

```python
# Cause 1: Malformed XML input
import xml.etree.ElementTree as ET

raw_xml = "<root><item>value</root>"  # Missing closing tag for <item>
tree = ET.fromstring(raw_xml)  # ParseError: mismatched tag

# Cause 2: Invalid characters in XML
import xml.etree.ElementTree as ET

raw_xml = "<root>text with \x00 null byte</root>"
ET.fromstring(raw_xml)  # ParseError: invalid character

# Cause 3: SAX parser encountering bad input
import xml.sax

class Handler(xml.sax.ContentHandler):
    pass

parser = xml.sax.make_parser()
parser.setContentHandler(Handler())
parser.feed("<root>&unknown_entity;</root>")  # SAXParseException: undefined entity

# Cause 4: DOM parsing with namespace issues
from xml.dom import minidom

doc = minidom.parseString("<root xmlns:ns='http://example.com'><ns:item/></root>")
# Accessing elements without namespace prefix
items = doc.getElementsByTagName("item")  # Returns empty NodeList

# Cause 5: Encoding declaration mismatch
import xml.etree.ElementTree as ET

raw_xml = '<?xml version="1.0" encoding="ascii"?><root>Ünïcödé</root>'
ET.fromstring(raw_xml)  # ParseError: encoding mismatch
```

## How to Fix

### Fix 1: Validate XML before parsing

```python
import xml.etree.ElementTree as ET
from io import StringIO

def safe_parse_xml(xml_string):
    try:
        return ET.fromstring(xml_string)
    except ET.ParseError as e:
        print(f"XML Parse Error: {e}")
        return None

# Use it
root = safe_parse_xml("<root><item>value</item></root>")
if root is not None:
    print(root.find("item").text)
```

### Fix 2: Use iterparse for large files

```python
import xml.etree.ElementTree as ET

# Process large XML files without loading entire tree into memory
for event, elem in ET.iterparse("large_file.xml", events=("end",)):
    if elem.tag == "record":
        process_record(elem)
        elem.clear()  # Free memory
```

### Fix 3: Handle namespaces correctly with ElementTree

```python
import xml.etree.ElementTree as ET

raw_xml = """
<root xmlns:ns="http://example.com">
    <ns:item ns:attr="value">text</ns:item>
</root>
"""
root = ET.fromstring(raw_xml)

# Define namespace mapping
ns = {"ns": "http://example.com"}
items = root.findall("ns:item", ns)

for item in items:
    print(item.text)
    print(item.get(f"{{{ns['ns']}}}attr"))
```

### Fix 4: Use minidom for DOM manipulation

```python
from xml.dom import minidom

doc = minidom.parseString("<root xmlns:ns='http://example.com'><ns:item>text</ns:item></root>")

# Use getElementsByTagNameNS for namespaced elements
items = doc.getElementsByTagNameNS("http://example.com", "item")
for item in items:
    print(item.firstChild.nodeValue)
```

### Fix 5: Configure SAX parser for error handling

```python
import xml.sax

class SafeHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.errors = []

    def startDocument(self):
        pass

    def endDocument(self):
        pass

    def startElement(self, name, attrs):
        pass

    def endElement(self, name):
        pass

    def characters(self, content):
        pass

parser = xml.sax.make_parser()
parser.setContentHandler(SafeHandler())
parser.setFeature(xml.sax.handler.feature_validation, False)
parser.setFeature(xml.sax.handler.feature_namespaces, 1)

try:
    parser.parse("data.xml")
except xml.sax.SAXParseException as e:
    print(f"Line {e.getLineNumber()}, Col {e.getColumnNumber()}: {e.getMessage()}")
```

## Examples

```python
# Real-world: Parse RSS feed
import xml.etree.ElementTree as ET

def parse_rss(xml_string):
    root = ET.fromstring(xml_string)
    items = []
    for item in root.findall(".//item"):
        title = item.find("title").text if item.find("title") is not None else ""
        link = item.find("link").text if item.find("link") is not None else ""
        description = item.find("description").text if item.find("description") is not None else ""
        items.append({"title": title, "link": link, "description": description})
    return items

# Real-world: Create XML document
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def create_config():
    root = Element("configuration")
    db = SubElement(root, "database")
    host = SubElement(db, "host")
    host.text = "localhost"
    port = SubElement(db, "port")
    port.text = "5432"

    rough_string = tostring(root, encoding="unicode")
    parsed = minidom.parseString(rough_string)
    return parsed.toprettyxml(indent="  ")
```

## Related Errors

- [ParseError](/languages/python/syntaxerror/) — XML syntax errors during parsing
- [UnicodeDecodeError](/languages/python/unicodedecodeerror/) — encoding issues in XML content
- [FileNotFoundError](/languages/python/filenotfounderror/) — missing XML files
