---
title: "[Solution] Heroku Buildpack Not Found Error"
description: "Fix Heroku buildpack not found errors. Resolve buildpack detection issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Buildpack Not Found Error can prevent your application from working correctly.

## Common Causes

- Buildpack not installed
- Buildpack URL incorrect
- No matching buildpack

## How to Fix

### Set Buildpack

```bash
heroku buildpacks:set heroku/nodejs --app my-app
```

