---
title: "[Solution] Heroku Pipeline Promotion Error"
description: "Fix Heroku pipeline promotion errors. Resolve stage promotion issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Pipeline Promotion Error can prevent your application from working correctly.

## Common Causes

- Promotion failed
- Slug not available
- Target app error

## How to Fix

### Promote

```bash
heroku pipelines:promote --app my-app-staging
```

