---
title: "[Solution] Maven Build Failed in Jenkins Pipeline"
description: "Fix Maven build failures in Jenkins pipeline. Resolve dependency, compilation, and test failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Build Failed in Jenkins Pipeline

Maven build failures occur when `mvn` commands exit with a non-zero status.

## Common Causes

- Dependency download failure
- Compilation errors
- Test failures
- Out of memory during compilation

## How to Fix

```groovy
pipeline {
    agent any
    tools { maven 'Maven-3.9'; jdk 'JDK-17' }
    stages {
        stage('Build') {
            steps { sh 'mvn clean compile -B' }
        }
    }
}
```

```bash
export MAVEN_OPTS="-Xmx2g -XX:MaxMetaspaceSize=512m"
mvn clean package -B
```
