---
title: "[Solution] Docker Compose Security Options Error"
description: "Fix Docker Compose security_opt errors. Resolve security option issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Security Options Error can prevent your application from working correctly.

## Common Causes

- Security option not valid
- Seccomp profile wrong

## How to Fix

### Set Security Options

```yaml
services:
  web:
    security_opt:
      - no-new-privileges:true
```

