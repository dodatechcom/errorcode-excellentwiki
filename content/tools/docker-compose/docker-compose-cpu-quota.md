---
title: "[Solution] Docker Compose CPU Quota Error"
description: "Fix Docker Compose cpu_quota errors. Resolve CPU quota configuration issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose CPU Quota Error can prevent your application from working correctly.

## Common Causes

- Quota value invalid
- Quota exceeds available CPU

## How to Fix

### Set CPU Quota

```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '0.5'
```

