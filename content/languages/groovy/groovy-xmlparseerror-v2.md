---
title: "[Solution] Groovy XmlSlurper Parse Error"
description: "Fix Groovy XmlSlurper parse errors when parsing malformed XML. Handle encoding, namespaces, and validation."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An XML parse error in Groovy's XmlSlurper occurs when the XML document is malformed, has encoding issues, or contains invalid characters.

## Common Causes

- Malformed XML (unclosed tags, missing root)
- Invalid characters in XML content
- Encoding mismatch (UTF-8 vs Latin-1)
- Namespace issues
- XML declarations with wrong encoding

## How to Fix

```groovy
// WRONG: Parsing malformed XML
def xml = '<root><item>value</root>'  // Missing closing tag
def slurper = new XmlSlurper()
def root = slurper.parseText(xml)  // Error

// CORRECT: Fix XML structure
def xml = '<root><item>value</item></root>'
def slurper = new XmlSlurper()
def root = slurper.parseText(xml)
```

```groovy
// WRONG: Not handling encoding
def xml = '<root><name>café</name></root>'  // May fail with encoding
def slurper = new XmlSlurper()
def root = slurper.parseText(xml)

// CORRECT: Handle encoding properly
def xml = '<?xml version="1.0" encoding="UTF-8"?><root><name>café</name></root>'
def slurper = new XmlSlurper()
def root = slurper.parseText(xml)
```

```groovy
// WRONG: Parsing XML with special characters
def xml = '<root><data>a & b</data></root>'  // & is invalid

// CORRECT: Escape special characters
def xml = '<root><data>a &amp; b</data></root>'
def root = new XmlSlurper().parseText(xml)
```

## Examples

```groovy
// Example 1: Safe XML parsing
def safeParseXml(String xml) {
    try {
        def slurper = new XmlSlurper()
        return slurper.parseText(xml)
    } catch (Exception e) {
        println "XML parse error: ${e.message}"
        return null
    }
}

// Example 2: XML with namespaces
def xml = '''<root xmlns:ns="http://example.com">
    <ns:item>value</ns:item>
</root>'''
def slurper = new XmlSlurper()
def root = slurper.parseText(xml)
println root.'ns:item'

// Example 3: XmlParser for validation
def parser = new XmlParser(false, false)  // Don't validate
def root = parser.parseText(xml)
```

## Related Errors

- [groovy-jsonerror]({{< relref "/languages/groovy/groovy-jsonerror" >}}) — JSON parse error
- [groovy-casterror]({{< relref "/languages/groovy/groovy-casterror" >}}) — cast error
- [groovy-nullpointererror]({{< relref "/languages/groovy/groovy-nullpointererror" >}}) — null pointer
