---
title: "[Solution] Docker Compose Journald Logging Error"
description: "Fix Docker Compose journald logging errors. Resolve journald log driver issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Journald Logging Error can prevent your application from working correctly.

## Common Causes

- Journald not available
- Log format wrong

## How to Fix

### Use Journald

```yaml
logging:
  driver: journald
```

