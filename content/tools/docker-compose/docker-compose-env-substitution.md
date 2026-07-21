---
title: "[Solution] Docker Compose Environment Variable Substitution Error"
description: "Fix Docker Compose env variable substitution errors. Resolve variable resolution issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Environment Variable Substitution Error can prevent your application from working correctly.

## Common Causes

- Variable not defined
- Substitution syntax wrong
- Default value missing

## How to Fix

### Use Variable

```yaml
services:
  web:
    image: ${IMAGE:-nginx}
```

### Set Default

```yaml
MY_VAR: ${MY_VAR:-default_value}
```

