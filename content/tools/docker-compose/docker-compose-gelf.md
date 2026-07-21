---
title: "[Solution] Docker Compose GELF Logging Error"
description: "Fix Docker Compose GELF logging errors. Resolve GELF log driver issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose GELF Logging Error can prevent your application from working correctly.

## Common Causes

- GELF server unreachable
- Format invalid

## How to Fix

### Use GELF

```yaml
logging:
  driver: gelf
  options:
    gelf-address: "udp://192.168.1.10:12201"
```

