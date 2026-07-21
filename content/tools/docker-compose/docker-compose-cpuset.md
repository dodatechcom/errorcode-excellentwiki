---
title: "[Solution] Docker Compose Cpuset Error"
description: "Fix Docker Compose cpuset errors. Resolve CPU set pinning issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Cpuset Error can prevent your application from working correctly.

## Common Causes

- CPU set invalid
- CPU not available

## How to Fix

### Set CPUset

```yaml
services:
  web:
    cpuset: "0,1"
```

