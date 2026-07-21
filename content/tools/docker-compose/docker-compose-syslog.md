---
title: "[Solution] Docker Compose Syslog Logging Error"
description: "Fix Docker Compose syslog logging errors. Resolve syslog log driver issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Syslog Logging Error can prevent your application from working correctly.

## Common Causes

- Syslog server unreachable
- Format invalid

## How to Fix

### Use Syslog

```yaml
logging:
  driver: syslog
  options:
    syslog-address: "tcp://192.168.1.10:514"
```

