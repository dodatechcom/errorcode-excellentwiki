---
title: "[Solution] Docker Compose Always Restart Error"
description: "Fix Docker Compose always restart errors. Resolve restart loop issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Always Restart Error can prevent your application from working correctly.

## Common Causes

- Container restarting continuously
- Application crashing

## How to Fix

### Fix Application

Check application logs:

```bash
docker compose logs web
```

