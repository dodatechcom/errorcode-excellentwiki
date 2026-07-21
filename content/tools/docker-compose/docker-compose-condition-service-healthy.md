---
title: "[Solution] Docker Compose Condition service_healthy Error"
description: "Fix Docker Compose condition service_healthy errors. Resolve health condition issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Condition service_healthy Error can prevent your application from working correctly.

## Common Causes

- Health check not configured
- Service not healthy

## How to Fix

### Use Healthy Condition

```yaml
services:
  web:
    depends_on:
      db:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
```

