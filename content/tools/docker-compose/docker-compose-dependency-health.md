---
title: "[Solution] Docker Compose Dependency Health Error"
description: "Fix Docker Compose dependency health errors. Resolve health check dependency issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Dependency Health Error can prevent your application from working correctly.

## Common Causes

- Health check not passing
- Service not healthy
- Timeout waiting

## How to Fix

### Add Health Check

```yaml
services:
  db:
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
      interval: 10s
      timeout: 5s
      retries: 5
```

