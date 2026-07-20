---
title: "[Solution] NotSerializableException in Jenkins Pipeline"
description: "Fix java.io.NotSerializableException in Jenkins pipelines. Resolve serialization errors when passing objects between pipeline steps."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# NotSerializableException in Jenkins Pipeline

A `java.io.NotSerializableException` occurs when a Jenkins pipeline tries to serialize an object that does not implement `java.io.Serializable`. Jenkins pipelines run on the CPS-transformed engine which requires all objects crossing step boundaries to be serializable.

## Common Causes

- Using non-serializable types (e.g., `Thread`, `Socket`, `FileInputStream`) as variables in pipeline steps
- Storing closures or lambda references that capture non-serializable state
- Using third-party library objects that are not `Serializable`
- Returning non-serializable objects from `sh` or `bat` steps into Groovy variables

## How to Fix

### Mark Your Class as Serializable

```java
package com.example
import java.io.Serializable
class BuildConfig implements Serializable {
    String version
    String environment
}
```

### Use @NonCPS for Non-Serializable Operations

```groovy
@NonCPS
def parseJson(String text) {
    return new groovy.json.JsonSlurperClassic().parseText(text)
}
```

## Examples

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    def threadName = Thread.currentThread().name
                    echo threadName
                }
            }
        }
    }
}
```
