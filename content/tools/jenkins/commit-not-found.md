---
title: "[Solution] Git Commit Not Found in Jenkins Pipeline"
description: "Fix git commit not found errors in Jenkins pipeline. Resolve SHA checkout failures and ref issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Commit Not Found in Jenkins Pipeline

Jenkins fails when trying to check out a specific commit SHA that does not exist.

## Common Causes

- Commit was rebased or force-pushed away
- Shallow clone does not include the target commit
- Webhook payload contains a stale SHA

## How to Fix

```groovy
branches: [[name: 'main']]
```

```groovy
extensions: [
    [$class: 'CloneOption', depth: 0],
    [$class: 'BuildChooserSetting', buildChooser: [$class: 'DefaultBuildChooser']]
]
```
