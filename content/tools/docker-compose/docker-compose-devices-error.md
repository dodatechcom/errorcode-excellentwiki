---
title: "[Solution] Docker Compose Devices Error"
description: "Fix Docker Compose devices errors. Resolve device mounting issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Devices Error can prevent your application from working correctly.

## Common Causes

- Device not found
- Permission denied
- Device path wrong

## How to Fix

### Mount Device

```yaml
services:
  web:
    devices:
      - "/dev/sda:/dev/sda"
```

