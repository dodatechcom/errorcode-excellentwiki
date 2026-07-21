---
title: "[Solution] Netlify Position Parameter Error"
description: "Fix Netlify position parameter errors. Resolve image crop position issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Position Parameter Error can prevent your application from working correctly.

## Common Causes

- Position value invalid
- Position not applied
- Crop area wrong

## How to Fix

### Set Position

```
/.netlify/images?url=/image.jpg&w=300&h=300&fit=cover&position=top
```

### Options

top, bottom, left, right, center

