---
title: "[Solution] Gradle Build Failed in Jenkins Pipeline"
description: "Fix Gradle build failures in Jenkins pipeline. Resolve dependency, task, and memory issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Build Failed in Jenkins Pipeline

Gradle build failures occur when the `gradle` or `./gradlew` command exits with a non-zero status.

## Common Causes

- Dependency resolution failure
- Gradle daemon OOM
- Wrapper version mismatch
- Corrupted cached dependencies

## How to Fix

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps { sh './gradlew clean build -x test --no-daemon' }
        }
    }
}
```

```groovy
environment { GRADLE_OPTS = '-Xmx2g -Dorg.gradle.daemon=false' }
```
