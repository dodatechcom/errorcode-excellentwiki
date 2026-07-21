---
title: "[Solution] Docker Compose Restart Policy Error"
description: "Fix Docker Compose restart policy errors. Resolve restart configuration issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Restart Policy Error can prevent your application from working correctly.

## Common Causes

- Policy not valid
- Restart loop
- Policy format wrong

## How to Fix

### Set Restart Policy

```yaml
services:
  web:
    restart: unless-stopped
```

