---
title: "[Solution] Heroku Shield Space Error"
description: "Fix Heroku shield space errors. Resolve shield space compliance issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Shield Space Error can prevent your application from working correctly.

## Common Causes

- Shield space not configured
- Compliance requirement not met

## How to Fix

### Check Shield Space

```bash
heroku spaces:info --space my-space
```

