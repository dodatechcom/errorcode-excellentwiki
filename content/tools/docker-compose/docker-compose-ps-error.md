---
title: "[Solution] Docker Compose Ps Error"
description: "Fix docker compose ps errors. Resolve container listing issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Ps Error can prevent your application from working correctly.

## Common Causes

- No containers running
- Compose file not found

## How to Fix

### List Containers

```bash
docker compose ps -a
```

