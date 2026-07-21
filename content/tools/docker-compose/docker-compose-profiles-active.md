---
title: "[Solution] Docker Compose Profiles Active Error"
description: "Fix Docker Compose profiles active errors. Resolve active profile issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Profiles Active Error can prevent your application from working correctly.

## Common Causes

- Profile not activated
- Wrong profile

## How to Fix

### Activate Profiles

```bash
docker compose --profile debug up
```

