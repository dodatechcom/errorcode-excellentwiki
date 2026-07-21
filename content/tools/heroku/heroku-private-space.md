---
title: "[Solution] Heroku Private Space Error"
description: "Fix Heroku private space errors. Resolve private space configuration issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku Private Space Error can prevent your application from working correctly.

## Common Causes

- Space not configured
- Network peering failed
- Firewall issue

## How to Fix

### Check Space

```bash
heroku spaces:info --space my-space
```

