---
title: "[Solution] Heroku Space Delete Error"
description: "Fix Heroku space delete errors. Resolve space deletion issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Space Delete Error can prevent your application from working correctly.

## Common Causes

- Space not empty
- Apps still running
- Permission denied

## How to Fix

### Delete Space

```bash
heroku spaces:destroy my-space
```

