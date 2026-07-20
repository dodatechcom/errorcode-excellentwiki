---
title: "[Solution] Script Not Allowed in Declarative Pipeline"
description: "Fix 'script not allowed' error in Jenkins declarative pipeline. Resolve script block restrictions."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Script Not Allowed in Declarative Pipeline

The `script` step is allowed in declarative pipelines but the code inside must conform to CPS transformation rules. Certain operations are restricted.

## Common Causes

- Using `script` block to call methods that are not CPS-transformed
- Attempting to modify pipeline variables outside `script` block
- Using Java reflection or system calls blocked by the sandbox

## How to Fix

```groovy
@NonCPS
def forbiddenOperation() {
    return "result"
}
```

```groovy
stage('Build') {
    steps {
        script {
            def version = readFile('version.txt').trim()
            env.APP_VERSION = version
        }
        sh 'make build'
    }
}
```

## Examples

```groovy
pipeline {
    agent any
    stages {
        stage('Set Version') {
            steps {
                script {
                    env.VERSION = '1.0'
                }
            }
        }
    }
}
```
