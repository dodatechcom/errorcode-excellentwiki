---
title: "[Solution] Jenkins JAR Cache Error"
description: "Fix Jenkins JAR cache errors. Resolve Java dependency cache and resolution issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins JAR Cache Error

JAR cache errors occur when Jenkins cannot cache or resolve JAR dependencies.

## How to Fix

```bash
rm -rf ~/.m2/repository
rm -rf ~/.gradle/caches
```

```groovy
environment { MAVEN_OPTS = "-Dmaven.repo.local=${WORKSPACE}/.m2/repository" }
```
