---
title: "[Solution] Heroku Release Phase Error"
description: "Fix Heroku release phase errors. Resolve release script execution issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Release Phase Error can prevent your application from working correctly.

## Common Causes

- Release script failed
- Script not found
- Timeout

## How to Fix

### Check Release Phase

```bash
heroku logs --tail --app my-app
```

