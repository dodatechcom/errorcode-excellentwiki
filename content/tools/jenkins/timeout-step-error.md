---
title: "[Solution] Jenkins Pipeline Timeout Step Error"
description: "Fix Jenkins pipeline timeout step errors. Resolve step timeout exceeded and pipeline abort issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Pipeline Timeout Step Error

The `timeout` step aborts a block of steps if it does not complete within the specified duration.

## Common Causes

- Timeout value too short for the operation
- Pipeline step is deadlocked
- External dependency is unresponsive

## How to Fix

```groovy
stage('Build') {
    steps {
        timeout(time: 30, unit: 'MINUTES') {
            sh 'make build'
        }
    }
}
```

```groovy
timeout(time: 10, unit: 'MINUTES') {
    try {
        sh 'make deploy'
    } finally {
        cleanWs()
    }
}
```
