---
title: "[Solution] Netlify Deploy CLI Error"
description: "Fix Netlify deploy CLI errors. Resolve deployment via CLI issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Deploy CLI Error can prevent your application from working correctly.

## Common Causes

- Deploy command failed
- Site not linked
- Build directory missing
- Token invalid

## How to Fix

### Deploy

```bash
netlify deploy --dir=dist --prod
```

### Link Site

```bash
netlify link
```

