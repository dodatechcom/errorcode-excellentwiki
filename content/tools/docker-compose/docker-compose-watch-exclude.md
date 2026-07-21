---
title: "[Solution] Docker Compose Watch Exclude Error"
description: "Fix docker compose watch exclude errors. Resolve watch exclusion issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Watch Exclude Error can prevent your application from working correctly.

## Common Causes

- Exclude pattern wrong
- Files not excluded

## How to Fix

### Configure Exclusion

```yaml
services:
  web:
    develop:
      watch:
        - action: sync
          path: ./src
          target: /app/src
          ignore:
            - node_modules
            - .git
```

