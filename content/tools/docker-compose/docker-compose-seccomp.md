---
title: "[Solution] Docker Compose Seccomp Error"
description: "Fix Docker Compose seccomp errors. Resolve seccomp profile issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Seccomp Error can prevent your application from working correctly.

## Common Causes

- Profile not found
- Profile format invalid

## How to Fix

### Use Seccomp Profile

```yaml
services:
  web:
    security_opt:
      - seccomp:profile.json
```

