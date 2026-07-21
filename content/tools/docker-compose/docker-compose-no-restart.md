---
title: "[Solution] Docker Compose No Restart Error"
description: "Fix Docker Compose no restart errors. Resolve container not restarting issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose No Restart Error can prevent your application from working correctly.

## Common Causes

- Container not restarting after crash
- restart: no set

## How to Fix

### Enable Restart

```yaml
services:
  web:
    restart: unless-stopped
```

