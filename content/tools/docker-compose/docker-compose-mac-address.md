---
title: "[Solution] Docker Compose MAC Address Error"
description: "Fix Docker Compose MAC address errors. Resolve MAC address configuration issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose MAC Address Error can prevent your application from working correctly.

## Common Causes

- MAC address format invalid
- MAC address conflict

## How to Fix

### Set MAC Address

```yaml
services:
  web:
    mac_address: 02:42:ac:11:00:02
```

