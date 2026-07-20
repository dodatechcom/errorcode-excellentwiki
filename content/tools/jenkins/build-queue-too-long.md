---
title: "[Solution] Jenkins Build Queue Too Long"
description: "Fix Jenkins build queue backlog issues. Resolve long queue wait times and build scheduling."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Build Queue Too Long

Build queue issues occur when too many builds are queued and waiting for available executors.

## Common Causes

- Not enough executors
- Long-running builds holding executors
- Incorrect agent labels

## How to Fix

```groovy
properties([
    disableConcurrentBuilds(),
    buildDiscarder(logRotator(numToKeepStr: '10'))
])
```

```groovy
lock(resource: 'deploy-env', inversePrecedence: true) {
    sh './deploy.sh'
}
```
