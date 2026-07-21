---
title: "[Solution] Groovy Missing Import"
description: "Required class not imported."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Missing Import

Required class not imported.

### Common Causes
Missing import statement; wrong package

### How to Fix
```groovy
import groovy.json.JsonSlurper
```

### Examples
```groovy
import groovy.json.JsonOutput
def json = JsonOutput.toJson([name: "test"])
```
