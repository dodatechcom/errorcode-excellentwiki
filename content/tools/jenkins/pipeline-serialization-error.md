---
title: "[Solution] Jenkins Pipeline Serialization Error"
description: "Fix Jenkins pipeline serialization errors when Groovy objects cannot be serialized for durable task execution."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Pipeline Serialization Error

Pipeline serialization errors occur when a Jenkins Pipeline step tries to persist state but encounters objects that cannot be serialized, typically during durable task execution.

## Common Causes

- Non-serializable objects used in pipeline steps (closures, threads)
- Script console uses classes that do not implement `Serializable`
- `@NonCPS` functions return non-serializable data
- Shared library imports include non-serializable classes

## How to Fix

### Solution 1: Implement Serializable on custom classes

```groovy
class BuildResult implements Serializable {
    String status
    int exitCode
}

def result = new BuildResult()
result.status = "success"
```

### Solution 2: Use @NonCPS for non-serializable operations

```groovy
@NonCPS
def parseJson(String text) {
    return new groovy.json.JsonSlurperClassic().parseText(text)
}
```

### Solution 3: Avoid closures in pipeline steps

```groovy
// Wrong - closure is not serializable
pipeline {
    stages {
        stage('Build') {
            steps {
                script {
                    def items = [1, 2, 3]
                    items.each { println it }  // May fail
                }
            }
        }
    }
}

// Fixed
pipeline {
    stages {
        stage('Build') {
            steps {
                script {
                    for (int i = 1; i <= 3; i++) {
                        println i
                    }
                }
            }
        }
    }
}
```

## Examples

```
java.io.NotSerializableException: org.jenkinsci.plugins.workflow.cps.CpsScript
```

## Prevent It

- Use `@NonCPS` for utility functions
- Keep pipeline steps simple and stateless
- Test pipelines with durable task checkpoints enabled
