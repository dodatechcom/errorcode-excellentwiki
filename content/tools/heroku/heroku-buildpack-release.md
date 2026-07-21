---
title: "[Solution] Heroku Buildpack Release Error"
description: "Fix Heroku buildpack release errors. Resolve release phase issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Buildpack Release Error can prevent your application from working correctly.

## Common Causes

- Release script failed
- Migrations failed
- Process not starting

## How to Fix

### Check Release Phase

```bash
heroku logs --tail --app my-app
```

