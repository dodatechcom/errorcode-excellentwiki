---
title: "[Solution] Docker Compose Port Already Allocated Error"
description: "Fix Docker Compose port already allocated errors. Resolve port conflict issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Port Already Allocated Error can prevent your application from working correctly.

## Common Causes

- Port in use by another container
- Port in use by host service

## How to Fix

### Find Port Usage

```bash
lsof -i :8080
netstat -tlnp | grep 8080
```

### Change Port

```yaml
ports:
  - "8081:80"
```

