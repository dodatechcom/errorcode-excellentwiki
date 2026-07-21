---
title: "[Solution] Docker Compose Profiles Services Error"
description: "Fix Docker Compose profiles services errors. Resolve profile-service mapping issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Profiles Services Error can prevent your application from working correctly.

## Common Causes

- Service not in any profile
- Service in wrong profile

## How to Fix

### Check Profiles

```bash
docker compose profiles
```

