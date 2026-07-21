---
title: "[Solution] Docker Compose File Not Found"
description: "Fix Docker Compose file not found errors. Resolve compose file lookup issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose File Not Found can prevent your application from working correctly.

## Common Causes

- compose.yml or docker-compose.yml missing
- File in wrong directory
- File renamed

## How to Fix

### Check Files

```bash
ls -la docker-compose.yml compose.yml
```

### Specify Path

```bash
docker compose -f /path/to/compose.yml up
```

