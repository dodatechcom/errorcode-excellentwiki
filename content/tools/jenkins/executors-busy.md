---
title: "[Solution] Jenkins Executors All Busy"
description: "Fix Jenkins executors all busy errors. Resolve executor capacity and build scheduling issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Executors All Busy

All executors on matching agents are busy.

## How to Fix

```groovy
properties([disableConcurrentBuilds()])
```

```groovy
lock(resource: 'build-server', inversePrecedence: true) { sh 'make build' }
```

```bash
# Manage Jenkins > Manage Nodes > Node > Configure > # of executors
```
