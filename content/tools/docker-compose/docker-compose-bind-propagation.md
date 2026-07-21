---
title: "[Solution] Docker Compose Bind Propagation Error"
description: "Fix Docker Compose bind propagation errors. Resolve mount propagation issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Bind Propagation Error can prevent your application from working correctly.

## Common Causes

- Propagation mode invalid
- Mount propagation not supported

## How to Fix

### Set Propagation

```yaml
volumes:
  - ./data:/app/data:rw,shared
```

