---
title: "[Solution] Groovy XML Parsing"
description: "XmlSlurper/XmlParser errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy XML Parsing

XmlSlurper/XmlParser errors.

### Common Causes
Wrong path; namespace issues

### How to Fix
```groovy
import groovy.xml.XmlSlurper
def xml = new XmlSlurper().parseText('<root><item>text</item></root>')
println root.item.text()
```

### Examples
```groovy
import groovy.xml.MarkupBuilder
def writer = new StringWriter()
def xml = new MarkupBuilder(writer)
xml.root { item('text') }
println writer.toString()
```
