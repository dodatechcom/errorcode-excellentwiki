---
title: "[Solution] Docker Compose Include Error"
description: "Fix docker compose include errors. Resolve include file issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Include Error can prevent your application from working correctly.

## Common Causes

- Include file not found
- Include syntax wrong

## How to Fix

### Use Include

```yaml
include:
  - path: docker-compose.override.yml
```

