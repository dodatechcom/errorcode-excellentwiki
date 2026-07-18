---
title: "[Solution] Groovy XmlSlurper Parse Error"
description: "Fix Groovy XmlSlurper parse errors. Handle malformed XML, namespace issues, and encoding problems."
languages: ["groovy"]
error-types: ["parse-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `XmlSlurper` parse error occurs when Groovy cannot parse XML content due to syntax errors, unclosed tags, or encoding issues. XML is stricter than HTML about well-formedness.

## Why It Happens

- Unclosed XML tags: Every opening tag must have a corresponding closing tag.
- Special characters not escaped in text content: Characters like `<`, `>`, `&` must be escaped.
- Namespace prefixes not properly declared: Namespaces must be declared before use.
- XML declaration encoding mismatch: The declared encoding does not match the actual encoding.
- Invalid characters in XML content: Certain characters are not allowed in XML.

## How to Fix It

Validate XML before parsing:

```groovy
import groovy.xml.XmlSlurper
import org.xml.sax.SAXException

def xmlText = '<root><item id="1">Test</item></root>'

try {
    def slurper = new XmlSlurper()
    def result = slurper.parseText(xmlText)
    println result.item.text()
} catch (SAXException e) {
    println "Invalid XML: ${e.message}"
}
```

Escape special characters in XML content:

```groovy
// WRONG: Unescaped ampersand
def badXml = '<data>Tom & Jerry</data>'

// CORRECT: Escape special characters
def goodXml = '<data>Tom &amp; Jerry</data>'

// Or use CDATA sections
def cdataXml = '<data><![CDATA[Tom & Jerry]]></data>'
```

Handle namespaces properly:

```groovy
def xml = '''<root xmlns:ns="http://example.com">
    <ns:item>Test</ns:item>
</root>'''

def slurper = new XmlSlurper()
slurper.setNamespaceAware(true)
def result = slurper.parseText(xml)
println result.'ns:item'.text()
```

Use XmlParser for more lenient parsing:

```groovy
import groovy.xml.XmlParser

def parser = new XmlParser()
parser.setKeepWhitespace(true)
def result = parser.parseText(xmlText)
```

Use XMLUtil for validation:

```groovy
import groovy.xml.XmlUtil

def validXml = XmlUtil.escapeXml("Tom & Jerry")
println validXml  // Tom &amp; Jerry
```

Use XMLUnit for validation:

```groovy
import org.xmlunit.builder.DiffBuilder
import org.xmlunit.builder.Input

def diff = DiffBuilder.compare(Input.fromString(expectedXml))
    .withTest(Input.fromString(actualXml))
    .build()
println diff.differences
```

Handle CDATA sections:

```groovy
def xml = '<data><![CDATA[<html>content</html>]]></data>'
def slurper = new XmlSlurper()
def result = slurper.parseText(xml)
println result.data.text()  // <html>content</html>
```

Use XmlSerializer for output:

```groovy
import groovy.xml.XmlUtil

def xmlBuilder = new groovy.xml.MarkupBuilder()
xmlBuilder.root {
    item(id: 1) {
        name("Test")
    }
}
def output = XmlUtil.serialize(xmlBuilder.toString())
```

## Common Mistakes

- Not handling XML with BOM markers. Strip BOM before parsing.
- Forgetting to declare namespaces before use. All namespaces must have a prefix declaration.
- Using text() on empty elements without default value. Use `text()` with `?: ''`.
- Not closing XmlSlurper resources after use. While not strictly required, it is good practice.
- Not handling processing instructions correctly. PI nodes require special handling.
- Not handling XML entities correctly. Some entities may not be recognized.
- Using XmlSlurper for large files. Consider streaming parsers for memory efficiency.

## Related Pages

- [groovy-json-parse-error]({{< relref "/languages/groovy/groovy-jsonerror-v2" >}}) - JSON parse errors
- [groovy-io-error]({{< relref "/languages/groovy/groovy-io-error" >}}) - I/O exception
- [groovy-null-pointer-v2]({{< relref "/languages/groovy/groovy-nullpointererror-v2" >}}) - null pointer
- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
