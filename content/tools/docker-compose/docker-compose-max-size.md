---
title: "[Solution] Docker Compose Max Size Error"
description: "Fix Docker Compose max-size errors. Resolve max log file size issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Max Size Error can prevent your application from working correctly.

## Common Causes

- Size format invalid
- Size too large

## How to Fix

### Set Max Size

```yaml
logging:
  options:
    max-size: "10m"
```

