---
title: "[Solution] Jenkins Build Unstable vs Failed Status"
description: "Fix Jenkins build unstable vs failed status. Resolve unstable build causes and reporting."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Build Unstable vs Failed Status

An unstable build is a middle state between success and failure. Jenkins marks builds as unstable when quality thresholds are not met.

## Common Causes

- Test failures marked as non-fatal
- Code coverage below threshold
- Warning thresholds exceeded

## How to Fix

```groovy
stage('Quality Check') {
    steps {
        script {
            def result = sh(script: 'checkstyle', returnStatus: true)
            if (result != 0) { unstable('Checkstyle warnings found') }
        }
    }
}
```
