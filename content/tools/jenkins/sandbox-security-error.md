---
title: "[Solution] Jenkins Groovy Sandbox Security Error"
description: "Fix Groovy sandbox security errors in Jenkins pipeline. Resolve ScriptSecurity and CPS transformation issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Groovy Sandbox Security Error

Jenkins applies a Groovy sandbox to pipeline scripts to prevent arbitrary code execution. When your script tries to access restricted Java classes or methods, the sandbox throws a `RejectedAccessException`.

## Common Causes

- Calling restricted Java APIs (e.g., `Runtime.getRuntime().exec()`)
- Accessing file system outside the Jenkins workspace
- Using dynamic class loading (`Class.forName`)
- Script not yet approved in the Script Approval console

## How to Fix

### Approve Scripts via Script Approval

Go to **Manage Jenkins > In-process Script Approval** and approve pending scripts.

### Use Approved Steps Instead of Raw Java

```groovy
sh 'echo test'
```

## Examples

```groovy
pipeline {
    agent any
    stages {
        stage('Security Test') {
            steps {
                sh 'ls -la'
            }
        }
    }
}
```
