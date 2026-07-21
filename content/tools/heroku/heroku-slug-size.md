---
title: "[Solution] Heroku Slug Size Too Large Error"
description: "Fix Heroku slug size too large errors. Resolve deployment size limit issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Slug Size Too Large Error can prevent your application from working correctly.

## Common Causes

- Slug exceeds 500 MB limit
- Too many dependencies
- Large binary files included

## How to Fix

### Check Slug Size

```bash
heroku ps --app my-app
```

### Reduce Size

- Remove unused files
- Use .slugignore
- Exclude dev dependencies

