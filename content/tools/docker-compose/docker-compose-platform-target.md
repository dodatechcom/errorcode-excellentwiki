---
title: "[Solution] Docker Compose Platform Target Error"
description: "Fix Docker Compose platform target errors. Resolve platform specification issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Platform Target Error can prevent your application from working correctly.

## Common Causes

- Platform not supported
- Platform format wrong

## How to Fix

### Set Platform

```yaml
services:
  web:
    image: nginx
    platform: linux/amd64
```

