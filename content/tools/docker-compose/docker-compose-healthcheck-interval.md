---
title: "[Solution] Docker Compose Healthcheck Interval Error"
description: "Fix Docker Compose healthcheck interval errors. Resolve check interval issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Healthcheck Interval Error can prevent your application from working correctly.

## Common Causes

- Interval too short
- Interval too long

## How to Fix

### Set Interval

```yaml
healthcheck:
  interval: 30s
```

