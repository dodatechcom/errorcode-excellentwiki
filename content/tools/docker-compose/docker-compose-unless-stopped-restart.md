---
title: "[Solution] Docker Compose Unless-Stopped Restart Error"
description: "Fix Docker Compose unless-stopped restart errors. Resolve restart behavior issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Unless-Stopped Restart Error can prevent your application from working correctly.

## Common Causes

- Container not restarting after daemon restart
- Manual stop not respected

## How to Fix

### Use Unless-Stopped

```yaml
services:
  web:
    restart: unless-stopped
```

