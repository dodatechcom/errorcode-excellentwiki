---
title: "[Solution] Docker Compose Network Not Found"
description: "Fix Docker Compose network not found errors. Resolve network lookup issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Network Not Found can prevent your application from working correctly.

## Common Causes

- Network not created
- Network name wrong
- External network issue

## How to Fix

### Define Network

```yaml
networks:
  mynetwork:
```

### Use External Network

```yaml
networks:
  mynetwork:
    external: true
```

