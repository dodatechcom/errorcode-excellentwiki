---
title: "[Solution] docker-compose include file Error"
description: "Fix docker compose include file errors. Resolve additional compose file issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

docker-compose include file Error can prevent your application from working correctly.

## Common Causes

- File not found
- Format invalid

## How to Fix

### Add Include

```yaml
include:
  - docker-compose.override.yml
```

