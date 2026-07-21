---
title: "[Solution] Docker Compose Scale Error"
description: "Fix Docker Compose scale errors. Resolve service scaling issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Scale Error can prevent your application from working correctly.

## Common Causes

- Cannot scale with ports
- Scale not supported for service

## How to Fix

### Remove Fixed Ports

```yaml
services:
  web:
    expose:
      - "80"
```

