---
title: "[Solution] Docker Compose Read Only Error"
description: "Fix Docker Compose read_only errors. Resolve read-only filesystem issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Read Only Error can prevent your application from working correctly.

## Common Causes

- Application needs write access
- tmpfs required

## How to Fix

### Use tmpfs for Writes

```yaml
services:
  web:
    read_only: true
    tmpfs:
      - /tmp
      - /var/cache
```

