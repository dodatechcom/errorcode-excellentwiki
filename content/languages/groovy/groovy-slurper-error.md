---
title: "[Solution] Groovy Slurper Error"
description: "XML/JSON Slurper errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Slurper Error

XML/JSON Slurper errors.

### Common Causes
Wrong parsing; encoding issues

### How to Fix
```groovy
import groovy.xml.XmlSlurper
def xml = '<root><item>test</item></root>'
def root = new XmlSlurper().parseText(xml)
```

### Examples
```groovy
import groovy.json.JsonSlurper
def json = '{"key": "value"}'
def parsed = new JsonSlurper().parseText(json)
```
