---
title: "[Solution] Docker Compose Healthcheck Retries Error"
description: "Fix Docker Compose healthcheck retries errors. Resolve retry count issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Healthcheck Retries Error can prevent your application from working correctly.

## Common Causes

- Too few retries
- Service marked unhealthy too quickly

## How to Fix

### Set Retries

```yaml
healthcheck:
  retries: 5
```

