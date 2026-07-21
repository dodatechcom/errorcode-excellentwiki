---
title: "[Solution] Docker Compose links Deprecated Error"
description: "Fix Docker Compose links deprecated errors. Resolve deprecated links usage."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose links Deprecated Error can prevent your application from working correctly.

## Common Causes

- links keyword deprecated
- Use depends_on instead

## How to Fix

### Use depends_on

```yaml
services:
  web:
    depends_on:
      - db
```

