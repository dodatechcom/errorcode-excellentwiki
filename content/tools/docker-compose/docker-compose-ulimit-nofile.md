---
title: "[Solution] Docker Compose Ulimit Nofile Error"
description: "Fix Docker Compose ulimit nofile errors. Resolve file descriptor limit issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Ulimit Nofile Error can prevent your application from working correctly.

## Common Causes

- Too many open files
- Limit too low

## How to Fix

### Increase Nofile

```yaml
services:
  web:
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
```

