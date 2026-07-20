---
title: "[Solution] Jenkins Build Timeout"
description: "Fix Jenkins build timeout errors. Resolve build duration exceeding configured limits."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Build Timeout

Build timeouts occur when a Jenkins build exceeds the configured maximum duration.

## Common Causes

- Long-running tests without timeout
- Infinite loops in build scripts
- Waiting for external resources

## How to Fix

```groovy
pipeline {
    agent any
    options { timeout(time: 60, unit: 'MINUTES'); timestamps() }
    stages {
        stage('Build') {
            timeout(time: 10, unit: 'MINUTES') { sh 'make build' }
        }
        stage('Test') {
            timeout(time: 15, unit: 'MINUTES') { sh 'make test' }
        }
    }
}
```
