---
title: "[Solution] Docker Compose Profile Error"
description: "Fix Docker Compose profile errors. Resolve profile selection issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Profile Error can prevent your application from working correctly.

## Common Causes

- Profile not found
- Service not in profile

## How to Fix

### Use Profiles

```yaml
services:
  web:
    image: nginx
    profiles: ["web"]
  debug:
    image: busybox
    profiles: ["debug"]
```

### Start with Profile

```bash
docker compose --profile web up
```

