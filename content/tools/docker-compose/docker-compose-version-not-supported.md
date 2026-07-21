---
title: "[Solution] Docker Compose Version Not Supported"
description: "Fix Docker Compose version errors. Resolve version compatibility issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Version Not Supported can prevent your application from working correctly.

## Common Causes

- Version field not supported
- Version deprecated
- Version format wrong

## How to Fix

### Remove Version Field

Newer Docker Compose does not require version field.

```yaml
services:
  web:
    image: nginx
```

