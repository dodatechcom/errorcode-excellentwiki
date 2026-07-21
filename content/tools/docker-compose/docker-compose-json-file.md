---
title: "[Solution] Docker Compose JSON File Logging Error"
description: "Fix Docker Compose json-file logging errors. Resolve JSON file log driver issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose JSON File Logging Error can prevent your application from working correctly.

## Common Causes

- Log file too large
- Rotation not configured

## How to Fix

### Configure Logging

```yaml
logging:
  driver: json-file
  options:
    max-size: "10m"
    max-file: "3"
```

