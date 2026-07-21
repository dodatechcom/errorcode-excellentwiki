---
title: "[Solution] Docker Compose Log Options Error"
description: "Fix Docker Compose log option errors. Resolve logging option configuration issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Log Options Error can prevent your application from working correctly.

## Common Causes

- Option not valid for driver
- Option value wrong

## How to Fix

### Set Log Options

```yaml
logging:
  driver: json-file
  options:
    max-size: "10m"
    max-file: "3"
    tag: "{{.ImageName}}"
```

