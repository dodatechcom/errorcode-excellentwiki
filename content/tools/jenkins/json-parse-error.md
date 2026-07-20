---
title: "[Solution] Jenkins JSON Parse Error in Pipeline"
description: "Fix Jenkins JSON parse errors in pipeline. Resolve JSON parsing and JsonSlurper issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins JSON Parse Error in Pipeline

JSON parse errors occur when pipeline scripts try to parse invalid JSON data.

## How to Fix

```groovy
@NonCPS
def parseJson(String text) {
    return new groovy.json.JsonSlurperClassic().parseText(text)
}
```

```groovy
script {
    try {
        def json = new groovy.json.JsonSlurperClassic().parseText(response)
    } catch (Exception e) {
        echo "Failed to parse JSON: ${e.message}"
    }
}
```
