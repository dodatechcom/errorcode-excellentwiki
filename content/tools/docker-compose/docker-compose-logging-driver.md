---
title: "[Solution] Docker Compose Logging Driver Error"
description: "Fix Docker Compose logging driver errors. Resolve logging configuration issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Logging Driver Error can prevent your application from working correctly.

## Common Causes

- Driver not available
- Driver configuration wrong

## How to Fix

### Set Logging Driver

```yaml
services:
  web:
    logging:
      driver: json-file
```

