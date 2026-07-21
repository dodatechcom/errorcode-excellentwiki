---
title: "[Solution] Docker Compose Sync Restart Error"
description: "Fix docker compose sync restart errors. Resolve file sync restart issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Sync Restart Error can prevent your application from working correctly.

## Common Causes

- Restart not triggered
- Sync not working

## How to Fix

### Configure Sync Restart

```yaml
services:
  web:
    develop:
      watch:
        - action: rebuild
          path: ./package.json
```

