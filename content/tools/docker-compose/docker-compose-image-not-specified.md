---
title: "[Solution] Docker Compose Image Not Specified"
description: "Fix Docker Compose image not specified errors. Resolve missing image definition."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Image Not Specified can prevent your application from working correctly.

## Common Causes

- No image or build specified
- Image name missing

## How to Fix

### Add Image

```yaml
services:
  web:
    image: nginx:latest
```

