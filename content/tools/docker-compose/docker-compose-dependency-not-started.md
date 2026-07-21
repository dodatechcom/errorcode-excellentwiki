---
title: "[Solution] Docker Compose Dependency Not Started Error"
description: "Fix Docker Compose dependency not started errors. Resolve service startup order issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Dependency Not Started Error can prevent your application from working correctly.

## Common Causes

- Dependent service failed to start
- Service crashed

## How to Fix

### Check Service Status

```bash
docker compose ps
```

### Check Logs

```bash
docker compose logs db
```

