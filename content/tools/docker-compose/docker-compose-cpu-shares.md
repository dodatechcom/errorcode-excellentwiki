---
title: "[Solution] Docker Compose CPU Shares Error"
description: "Fix Docker Compose cpu_shares errors. Resolve CPU share configuration issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose CPU Shares Error can prevent your application from working correctly.

## Common Causes

- Share value invalid
- CPU not available

## How to Fix

### Set CPU Shares

```yaml
services:
  web:
    cpu_shares: 512
```

