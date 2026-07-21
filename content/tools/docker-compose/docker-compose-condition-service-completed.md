---
title: "[Solution] Docker Compose Condition service_completed_successfully Error"
description: "Fix Docker Compose condition service_completed_successfully errors. Resolve completion condition issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Condition service_completed_successfully Error can prevent your application from working correctly.

## Common Causes

- Service did not complete successfully
- Exit code non-zero

## How to Fix

### Check Exit Code

```bash
docker compose ps -a
```

