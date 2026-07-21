---
title: "[Solution] Netlify Build Plugin Error"
description: "Fix Netlify build plugin errors. Resolve plugin configuration issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Build Plugin Error can prevent your application from working correctly.

## Common Causes

- Plugin not found
- Plugin version incompatible
- Plugin configuration invalid

## How to Fix

### Add Plugin

```toml
[[plugins]]
package = "netlify-plugin-cache"
  [plugins.inputs]
  paths = ["node_modules/.cache"]
```

