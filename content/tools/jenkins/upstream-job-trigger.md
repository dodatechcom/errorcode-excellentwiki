---
title: "[Solution] Jenkins Upstream Job Trigger Error"
description: "Fix Jenkins upstream job trigger errors. Resolve build trigger and dependency chain issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Upstream Job Trigger Error

Upstream triggers configure a job to start when another job completes.

## How to Fix

```bash
# Job > Configure > Build Triggers > Build after other projects > Watched items: upstream-job
```

```groovy
build job: 'upstream-job', wait: false
```
