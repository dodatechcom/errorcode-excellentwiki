---
title: "[Solution] Groovy JsonOutput Error"
description: "JsonOutput serialization errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy JsonOutput Error

JsonOutput serialization errors.

### Common Causes
Non-serializable object; date formatting

### How to Fix
```groovy
import groovy.json.JsonOutput
def data = [name: "test", items: [1, 2, 3]]
def json = JsonOutput.toJson(data)
```

### Examples
```groovy
def prettyJson = JsonOutput.prettyPrint(JsonOutput.toJson(data))
```
