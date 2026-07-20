---
title: "[Solution] Jenkins XML Marshal Error"
description: "Fix Jenkins XML marshalling errors. Resolve XML serialization and parsing issues in pipeline."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins XML Marshal Error

XML marshal errors occur when Jenkins cannot convert data to or from XML format.

## How to Fix

```groovy
import groovy.xml.MarkupBuilder
def writer = new StringWriter()
def xml = new MarkupBuilder(writer)
xml.configuration {
    server('prod')
    port(8080)
}
writeFile file: 'config.xml', text: writer.toString()
```

```groovy
def xmlContent = readFile 'config.xml'
def cleanXml = xmlContent.replaceAll('[^\x20-\x7E\x0A\x0D]', '')
```
