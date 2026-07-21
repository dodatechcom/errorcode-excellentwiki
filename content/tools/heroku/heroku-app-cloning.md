---
title: "[Solution] Heroku App Cloning Error"
description: "Fix Heroku app cloning errors. Resolve app duplication issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku App Cloning Error can prevent your application from working correctly.

## Common Causes

- Cloning failed
- Config not copied
- Addons not copied

## How to Fix

### Fork App

```bash
heroku fork --from source-app --to target-app
```

