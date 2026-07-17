---
title: "XmlSlurper parse error in Groovy"
description: "Fix XmlSlurper parse errors when Groovy cannot parse malformed or invalid XML content."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["xml", "XmlSlurper", "parse", "malformed", "groovy"]
weight: 5
---

## What This Error Means

Groovy's `XmlSlurper` parses XML strings and files into a GPath-accessible object tree. Parse errors occur when the XML is malformed or contains invalid characters.

## Common Causes

- Malformed XML (unclosed tags, mismatched tags)
- Invalid characters in XML content
- Encoding mismatch
- Entities not properly escaped

## How to Fix

```groovy
// WRONG: Malformed XML
def xml = "<root><item>value</root>"

// CORRECT: Well-formed XML
def xml = "<root><item>value</item></root>"
```

```groovy
// WRONG: Special characters not escaped
def xml = "<root><item>a & b</item></root>"

// CORRECT: Escape special characters
def xml = "<root><item>a &amp; b</item></root>"
```

## Examples

```groovy
def xml = '<employees><employee><name>Alice</name><age>30</age></employee></employees>'
def parsed = new XmlSlurper().parseText(xml)
println parsed.employee.name   // Alice
```

## Related Errors

- [JsonSlurper Error](/languages/groovy/jsonerror) - JSON parsing issues
