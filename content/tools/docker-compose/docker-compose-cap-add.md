---
title: "[Solution] Docker Compose Capabilities Add Error"
description: "Fix Docker Compose cap_add errors. Resolve Linux capability addition issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Capabilities Add Error can prevent your application from working correctly.

## Common Causes

- Capability not valid
- Security risk

## How to Fix

### Add Capability

```yaml
services:
  web:
    cap_add:
      - NET_ADMIN
      - SYS_PTRACE
```

