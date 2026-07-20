---
title: "[Solution] Jenkins Pipeline readFile Error"
description: "Fix readFile step errors in Jenkins pipeline. Resolve file reading issues in Jenkinsfile and shared libraries."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Pipeline readFile Error

The `readFile` step reads a file from the agent's workspace into a String. Errors occur when the file does not exist or permissions are insufficient.

## Common Causes

- File path is incorrect relative to the workspace
- File does not exist on the agent
- File permissions deny read access

## How to Fix

```groovy
stage('Read Config') {
    steps {
        script {
            if (fileExists('config.yml')) {
                def config = readFile 'config.yml'
                echo config
            } else {
                error 'config.yml not found'
            }
        }
    }
}
```
