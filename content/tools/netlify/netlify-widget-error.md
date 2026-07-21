---
title: "[Solution] Netlify CMS Widget Error"
description: "Fix Netlify CMS widget errors. Resolve editor widget issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify CMS Widget Error can prevent your application from working correctly.

## Common Causes

- Widget not found
- Widget configuration invalid
- Widget not rendering
- Widget value not saved

## How to Fix

### Add Widget

```yaml
- { name: date, widget: datetime, format: YYYY-MM-DD }
```

