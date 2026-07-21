---
title: "[Solution] Netlify Plugin Input Error"
description: "Fix Netlify plugin input errors. Resolve plugin configuration parameter issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Plugin Input Error can prevent your application from working correctly.

## Common Causes

- Input parameter missing
- Input value invalid
- Input type mismatch

## How to Fix

### Configure Input

```toml
[[plugins]]
package = "netlify-plugin-image-optim"
  [plugins.inputs]
  image_folder = "assets/images"
```

