---
title: "[Solution] Docker Compose Dockerfile Not Found"
description: "Fix Docker Compose Dockerfile not found errors. Resolve Dockerfile path issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Dockerfile Not Found can prevent your application from working correctly.

## Common Causes

- Dockerfile not in context
- Dockerfile path wrong

## How to Fix

### Specify Dockerfile

```yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.dev
```

