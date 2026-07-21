---
title: "[Solution] Heroku Stack Migration Error"
description: "Fix Heroku stack migration errors. Resolve stack upgrade issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Stack Migration Error can prevent your application from working correctly.

## Common Causes

- Migration failed
- Buildpack incompatible
- Config vars missing
- Migration in progress

## How to Fix

### Migrate Stack

```bash
heroku stack:set heroku-22 --app my-app
```

