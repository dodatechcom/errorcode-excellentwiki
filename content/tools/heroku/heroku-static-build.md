---
title: "[Solution] Heroku Static Build Error"
description: "Fix Heroku static build errors. Resolve static site deployment issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Static Build Error can prevent your application from working correctly.

## Common Causes

- Build command missing
- Output directory wrong
- No web server

## How to Fix

### Configure Static Build

```bash
heroku buildpacks:set heroku/nodejs --app my-app
heroku config:set NPM_CONFIG_PRODUCTION=false --app my-app
```

