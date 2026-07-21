---
title: "[Solution] Docker Compose Log Limit Error"
description: "Fix Docker Compose log limit errors. Resolve log size limit issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Log Limit Error can prevent your application from working correctly.

## Common Causes

- Log file too large
- Disk space running out

## How to Fix

### Configure Log Limits

```yaml
logging:
  driver: json-file
  options:
    max-size: "10m"
    max-file: "3"
```

