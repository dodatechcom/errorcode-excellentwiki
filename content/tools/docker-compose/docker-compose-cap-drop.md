---
title: "[Solution] Docker Compose Capabilities Drop Error"
description: "Fix Docker Compose cap_drop errors. Resolve Linux capability removal issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Capabilities Drop Error can prevent your application from working correctly.

## Common Causes

- Capability not droppable
- Application requires capability

## How to Fix

### Drop Capability

```yaml
services:
  web:
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
```

