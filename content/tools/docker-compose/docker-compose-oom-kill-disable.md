---
title: "[Solution] docker-compose oom_kill_disable Error"
description: "Fix Docker Compose oom_kill_disable errors. Resolve OOM killer disable issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

docker-compose oom_kill_disable Error can prevent your application from working correctly.

## Common Causes

- OOM killer disabled
- Memory leak risk

## How to Fix

### Disable OOM Kill

```yaml
services:
  web:
    oom_kill_disable: true
```

