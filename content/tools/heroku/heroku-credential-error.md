---
title: "[Solution] Heroku Credential Error"
description: "Fix Heroku credential errors. Resolve database authentication issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Credential Error can prevent your application from working correctly.

## Common Causes

- Invalid credentials
- Password changed
- Role does not exist

## How to Fix

### Reset Credentials

```bash
heroku pg:credentials:rotate --app my-app
```

