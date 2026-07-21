---
title: "[Solution] Docker Compose Gateway Error"
description: "Fix Docker Compose gateway errors. Resolve gateway configuration issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Gateway Error can prevent your application from working correctly.

## Common Causes

- Gateway not in subnet
- Gateway unreachable

## How to Fix

### Set Gateway

```yaml
networks:
  mynetwork:
    ipam:
      config:
        - subnet: 172.28.0.0/24
          gateway: 172.28.0.1
```

