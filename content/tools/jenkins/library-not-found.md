---
title: "[Solution] @Library Not Found in Jenkins Pipeline"
description: "Fix @Library annotation not found error in Jenkins shared library. Resolve shared library loading failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# @Library Not Found in Jenkins Pipeline

The `@Library` annotation imports a Jenkins shared library into a pipeline. When the library cannot be found, Jenkins fails to compile the Jenkinsfile.

## Common Causes

- Shared library not configured in Global Pipeline Libraries
- Library name or version does not match the configured name
- Repository URL is incorrect or inaccessible
- Network issues preventing Jenkins from cloning the library

## How to Fix

```bash
# Manage Jenkins > Configure System > Global Pipeline Libraries
# Name: my-shared-lib
# Default version: main
# Source: Git
# Repository URL: https://github.com/org/shared-lib.git
```

```groovy
@Library('my-shared-lib') _
@Library('my-shared-lib@main') _
@Library(['lib1', 'lib2@v2']) _
```
