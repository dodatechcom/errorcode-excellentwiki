---
title: "[Solution] Groovy JSON Parsing"
description: "JsonSlurper parsing errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy JSON Parsing

JsonSlurper parsing errors.

### Common Causes
Wrong format; encoding issues

### How to Fix
```groovy
import groovy.json.JsonSlurper
def json = new JsonSlurper().parseText('{"name": "test"}')
println json.name
```

### Examples
```groovy
import groovy.json.JsonOutput
def json = JsonOutput.toJson([name: "test", value: 42])
println JsonOutput.prettyPrint(json)
```
