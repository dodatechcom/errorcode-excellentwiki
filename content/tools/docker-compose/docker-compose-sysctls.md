---
title: "[Solution] Docker Compose Sysctls Error"
description: "Fix Docker Compose sysctls errors. Resolve kernel parameter issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Sysctls Error can prevent your application from working correctly.

## Common Causes

- Sysctl not allowed
- Sysctl format wrong
- Value invalid

## How to Fix

### Set Sysctls

```yaml
services:
  web:
    sysctls:
      - net.core.somaxconn=1024
      - net.ipv4.tcp_syncookies=0
```

