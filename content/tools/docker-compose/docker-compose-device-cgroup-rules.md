---
title: "[Solution] Docker Compose Device Cgroup Rules Error"
description: "Fix Docker Compose device_cgroup_rules errors. Resolve cgroup device rule issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Device Cgroup Rules Error can prevent your application from working correctly.

## Common Causes

- Rule format invalid
- Rule not supported

## How to Fix

### Set Cgroup Rules

```yaml
services:
  web:
    device_cgroup_rules:
      - "c 42:* rmw"
```

