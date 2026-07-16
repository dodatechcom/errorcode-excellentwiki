---
title: "[Solution] Jenkins Build Timeout"
description: "Fix Jenkins build timeout errors. Resolve long-running builds and timeout configuration issues."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "timeout", "build", "limit", "duration"]
weight: 5
---

# Jenkins Build Timeout

A build timeout occurs when a Jenkins build exceeds the configured timeout limit. Jenkins kills the build process to prevent it from running indefinitely.

## Common Causes

- The build is genuinely slow (large test suite, slow compilation)
- A step is hung (waiting for input, stuck network call)
- The timeout is set too low for the workload
- A deadlock or infinite loop in the build scripts

## How to Fix

### Configure Build Timeout in Pipeline

```groovy
pipeline {
    agent any
    options {
        timeout(time: 30, unit: 'MINUTES')
    }
    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
    }
}
```

### Set Timeout Per Stage

```groovy
stage('Tests') {
    steps {
        timeout(time: 20, unit: 'MINUTES') {
            sh 'npm test'
        }
    }
}
```

### Handle Timeout with Abort Action

```groovy
timeout(time: 10, unit: 'MINUTES') {
    waitUntil {
        // check condition
        return isReady()
    }
} 
```

### Increase Timeout for Large Projects

```groovy
options {
    timeout(time: 120, unit: 'MINUTES')  // 2 hours
}
```

### Diagnose Slow Builds

```bash
# Check build duration history
# Jenkins > Job > Build History > look at duration trends
```

## Examples

```bash
# Default timeout exceeded
# ERROR: Build timed out (after 120 minutes)
# Fix: set appropriate timeout in options or fix the hung step

# Wait for input timeout
# ERROR: Timed out waiting for user input
# Fix: add timeout around input step
```

## Related Errors

- [Build Failed]({{< relref "/tools/jenkins/build-failed" >}}) — build step returned error
- [Node Offline]({{< relref "/tools/jenkins/node-offline" >}}) — agent is not connected
