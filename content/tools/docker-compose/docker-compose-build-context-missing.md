---
title: "[Solution] Docker Compose Build Context Missing"
description: "Fix Docker Compose build context missing errors. Resolve build configuration issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Build Context Missing can prevent your application from working correctly.

## Common Causes

- build context not specified
- context path wrong

## How to Fix

### Add Build Context

```yaml
services:
  web:
    build: .
```

Or with context and Dockerfile:

```yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
```

