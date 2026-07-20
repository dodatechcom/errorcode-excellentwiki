---
title: "[Solution] Jenkins Tool Not Configured Error"
description: "Fix Jenkins tool not configured errors. Resolve missing build tool configuration in Jenkins."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Tool Not Configured Error

The `tools` directive requires the tool to be configured in Global Tool Configuration.

## Common Causes

- Tool not installed
- Tool name mismatch
- Tool auto-installation failed

## How to Fix

```bash
# Manage Jenkins > Global Tool Configuration > Add JDK, Maven, etc.
```

```groovy
pipeline {
    agent any
    tools { maven 'Maven-3.9'; jdk 'JDK-17'; nodejs 'Node-18' }
    stages {
        stage('Build') {
            steps { sh 'mvn --version' }
        }
    }
}
```
