---
title: "[Solution] Compiler Error in Jenkins Build"
description: "Fix compiler errors in Jenkins builds. Resolve Java, C++, and other compilation failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Compiler Error in Jenkins Build

Compiler errors occur when the source code cannot be compiled.

## Common Causes

- Syntax errors in source code
- Missing imports
- Incompatible compiler version

## How to Fix

```groovy
tools { jdk 'JDK-17'; maven 'Maven-3.9' }
```

```groovy
pipeline {
    agent any
    tools { jdk 'JDK-17' }
    stages {
        stage('Compile') { steps { sh 'mvn compile -B' } }
        stage('Package') { steps { sh 'mvn package -B -DskipTests' } }
    }
}
```
