---
title: "[Solution] Jenkins Executor Not Available"
description: "Fix Jenkins executor not available errors. Resolve build scheduling and agent allocation issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Executor Not Available

The `executor not available` error means Jenkins cannot find a free executor to run the build.

## Common Causes

- All executors busy
- Agent offline
- Label mismatch

## How to Fix

```groovy
pipeline { agent any ... }
```

```bash
# Manage Jenkins > Manage Clouds > Add Kubernetes or Docker cloud
```
