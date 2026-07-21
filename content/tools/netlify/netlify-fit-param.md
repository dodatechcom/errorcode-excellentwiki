---
title: "[Solution] Netlify Fit Parameter Error"
description: "Fix Netlify fit parameter errors. Resolve image resize behavior issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Fit Parameter Error can prevent your application from working correctly.

## Common Causes

- Fit value invalid
- Image distorted
- Fit not applied

## How to Fix

### Set Fit

```
/.netlify/images?url=/image.jpg&w=300&h=300&fit=cover
```

### Options

cover, contain, fill, inside, outside

