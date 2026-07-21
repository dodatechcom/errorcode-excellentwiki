---
title: "[Solution] Netlify Format Parameter Error"
description: "Fix Netlify format parameter errors. Resolve image format conversion issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Format Parameter Error can prevent your application from working correctly.

## Common Causes

- Format not supported
- Format parameter invalid
- Conversion failed

## How to Fix

### Set Format

```
/.netlify/images?url=/image.jpg&fm=webp
```

### Supported Formats

jpg, png, webp, avif, gif

