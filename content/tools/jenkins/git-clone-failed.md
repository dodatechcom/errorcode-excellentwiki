---
title: "[Solution] Git Clone Failed in Jenkins Pipeline"
description: "Fix git clone failed errors in Jenkins. Resolve repository clone failures and workspace issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Clone Failed in Jenkins Pipeline

A `git clone failed` error means Jenkins cannot create a new clone of the repository in the workspace.

## Common Causes

- Repository URL is wrong or deleted
- Authentication failure
- Disk space exhausted
- Repository is too large

## How to Fix

```groovy
checkout([
    $class: 'GitSCM',
    extensions: [[$class: 'CloneOption', shallow: true, depth: 1]],
    branches: [[name: 'main']],
    userRemoteConfigs: [[url: 'https://github.com/org/repo.git', credentialsId: 'git-creds']]
])
```
