---
title: "[Solution] Docker Compose Down Error"
description: "Fix docker compose down errors. Resolve container shutdown issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Down Error can prevent your application from working correctly.

## Common Causes

- Container not stopping
- Network not removing
- Volume in use

## How to Fix

### Force Down

```bash
docker compose down --volumes --remove-orphans
```

