---
title: "[Solution] Jenkins Build Trigger Cycle Detected"
description: "Fix Jenkins build trigger cycle errors. Resolve infinite trigger loops and circular dependencies."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Build Trigger Cycle Detected

Build trigger cycles occur when jobs trigger each other in a loop.

## How to Fix

```groovy
def isUpstreamTrigger() {
    return currentBuild.getBuildCauses('hudson.model.Cause$UpstreamCause').size() > 0
}

pipeline {
    agent any
    stages {
        stage('Build') {
            when { expression { !isUpstreamTrigger() } }
            steps { sh 'make build' }
        }
    }
}
```
