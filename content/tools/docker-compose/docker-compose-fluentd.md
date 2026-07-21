---
title: "[Solution] Docker Compose Fluentd Logging Error"
description: "Fix Docker Compose fluentd logging errors. Resolve fluentd log driver issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Fluentd Logging Error can prevent your application from working correctly.

## Common Causes

- Fluentd server unreachable
- Tag format wrong

## How to Fix

### Use Fluentd

```yaml
logging:
  driver: fluentd
  options:
    fluentd-address: localhost:24224
```

