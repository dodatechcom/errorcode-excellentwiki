---
title: "[Solution] Docker Compose Container Name Conflict"
description: "Fix Docker Compose container name conflict errors. Resolve naming collisions."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Container Name Conflict can prevent your application from working correctly.

## Common Causes

- Container name already in use
- Name from another compose file
- Manual container conflict

## How to Fix

### Change Container Name

```yaml
services:
  web:
    container_name: my-web
```

### Remove Conflicting Container

```bash
docker rm -f old-container
```

