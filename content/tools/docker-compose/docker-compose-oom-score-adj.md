---
title: "[Solution] Docker Compose OOM Score Adj Error"
description: "Fix Docker Compose oom_score_adj errors. Resolve OOM score adjustment issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose OOM Score Adj Error can prevent your application from working correctly.

## Common Causes

- Score out of range (-1000 to 1000)

## How to Fix

### Set OOM Score

```yaml
services:
  web:
    oom_score_adj: 500
```

