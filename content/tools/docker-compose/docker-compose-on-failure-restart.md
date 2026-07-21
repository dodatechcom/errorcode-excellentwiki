---
title: "[Solution] Docker Compose On-Failure Restart Error"
description: "Fix Docker Compose on-failure restart errors. Resolve failure-based restart issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose On-Failure Restart Error can prevent your application from working correctly.

## Common Causes

- Restart count exceeded
- Application failing repeatedly

## How to Fix

### Set Max Retries

```yaml
services:
  web:
    restart: on-failure:5
```

