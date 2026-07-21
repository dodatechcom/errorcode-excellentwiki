---
title: "[Solution] Docker Compose DNS Config Error"
description: "Fix Docker Compose DNS config errors. Resolve DNS configuration issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose DNS Config Error can prevent your application from working correctly.

## Common Causes

- DNS server unreachable
- DNS search domain wrong

## How to Fix

### Configure DNS

```yaml
services:
  web:
    dns:
      - 8.8.8.8
      - 8.8.4.4
```

