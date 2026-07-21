---
title: "[Solution] Docker Compose Ulimits Error"
description: "Fix Docker Compose ulimits errors. Resolve resource limit issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Ulimits Error can prevent your application from working correctly.

## Common Causes

- Ulimit value invalid
- Ulimit name wrong

## How to Fix

### Set Ulimits

```yaml
services:
  web:
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
```

