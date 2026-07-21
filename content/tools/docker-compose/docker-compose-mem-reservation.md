---
title: "[Solution] Docker Compose Memory Reservation Error"
description: "Fix Docker Compose mem_reservation errors. Resolve memory reservation issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Memory Reservation Error can prevent your application from working correctly.

## Common Causes

- Reservation higher than limit
- Reservation too low

## How to Fix

### Set Reservation

```yaml
services:
  web:
    deploy:
      resources:
        reservations:
          memory: 256M
```

