---
title: "[Solution] Docker Compose AppArmor Error"
description: "Fix Docker Compose AppArmor errors. Resolve AppArmor profile issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose AppArmor Error can prevent your application from working correctly.

## Common Causes

- Profile not loaded
- Profile not available

## How to Fix

### Set AppArmor Profile

```yaml
services:
  web:
    security_opt:
      - apparmor:my-profile
```

