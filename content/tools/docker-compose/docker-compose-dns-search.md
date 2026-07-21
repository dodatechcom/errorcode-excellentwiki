---
title: "[Solution] Docker Compose DNS Search Error"
description: "Fix Docker Compose DNS search errors. Resolve DNS search domain issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose DNS Search Error can prevent your application from working correctly.

## Common Causes

- Search domain not resolving
- Domain suffix wrong

## How to Fix

### Set DNS Search

```yaml
services:
  web:
    dns_search:
      - example.com
```

