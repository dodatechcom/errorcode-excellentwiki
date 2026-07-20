---
title: "[Solution] Jenkins Concurrent Build Disabled"
description: "Fix Jenkins concurrent build disabled errors. Resolve build queue and concurrent execution settings."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Concurrent Build Disabled

When concurrent builds are disabled, new builds cannot start while others are running.

## How to Fix

```groovy
options { disableConcurrentBuilds() }
```

```groovy
lock(resource: 'deploy-server', inversePrecedence: true) {
    sh './deploy.sh'
}
```
