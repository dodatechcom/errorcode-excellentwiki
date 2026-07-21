---
title: "[Solution] Heroku Buildpack Detect Error"
description: "Fix Heroku buildpack detect errors. Resolve automatic buildpack detection issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Buildpack Detect Error can prevent your application from working correctly.

## Common Causes

- Detection failed
- Multiple candidates
- No matching buildpack

## How to Fix

### Set Explicit Buildpack

```bash
heroku buildpacks:set heroku/nodejs --app my-app
```

