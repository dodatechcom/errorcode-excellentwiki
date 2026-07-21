---
title: "[Solution] Docker Compose Condition service_started Error"
description: "Fix Docker Compose condition service_started errors. Resolve startup condition issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Condition service_started Error can prevent your application from working correctly.

## Common Causes

- Service not started
- Condition not met

## How to Fix

### Use Condition

```yaml
services:
  web:
    depends_on:
      db:
        condition: service_started
```

