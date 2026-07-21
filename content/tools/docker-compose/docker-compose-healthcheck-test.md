---
title: "[Solution] Docker Compose Healthcheck Test Error"
description: "Fix Docker Compose healthcheck test errors. Resolve health check command issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Healthcheck Test Error can prevent your application from working correctly.

## Common Causes

- Command failed
- Test format wrong
- Command not found

## How to Fix

### Define Healthcheck

```yaml
services:
  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
```

