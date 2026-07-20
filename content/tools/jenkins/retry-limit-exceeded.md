---
title: "[Solution] Jenkins Pipeline Retry Limit Exceeded"
description: "Fix retry limit exceeded error in Jenkins pipeline. Resolve retry step exhaustion and transient failure handling."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Pipeline Retry Limit Exceeded

The `retry` step re-executes a block of steps up to N times. When all retry attempts are exhausted, the pipeline fails.

## Common Causes

- Transient network failures persist beyond retry count
- External service remains unavailable
- Retry count too low
- Retry applied to a non-transient error

## How to Fix

```groovy
stage('Build') {
    steps {
        retry(5) {
            sh 'make build'
            sleep(time: 10, unit: 'SECONDS')
        }
    }
}
```

### Retry Only on Specific Errors

```groovy
retry(3) {
    try {
        sh 'make build'
    } catch (err) {
        if (err.toString().contains('timeout')) {
            throw err
        }
        error "Non-retryable error: ${err.message}"
    }
}
```
