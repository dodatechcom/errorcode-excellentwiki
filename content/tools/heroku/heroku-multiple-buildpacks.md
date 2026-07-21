---
title: "[Solution] Heroku Multiple Buildpacks Error"
description: "Fix Heroku multiple buildpacks errors. Resolve buildpack ordering issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Multiple Buildpacks Error can prevent your application from working correctly.

## Common Causes

- Buildpacks conflicting
- Order incorrect
- Version mismatch

## How to Fix

### List Buildpacks

```bash
heroku buildpacks --app my-app
```

### Set Order

```bash
heroku buildpacks:add heroku/nodejs --app my-app
heroku buildpacks:add heroku/python --app my-app
```

