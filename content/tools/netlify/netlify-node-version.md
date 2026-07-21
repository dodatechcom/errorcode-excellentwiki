---
title: "[Solution] Netlify Node Version Error"
description: "Fix Netlify Node version errors. Resolve Node.js version mismatch issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Node Version Error can prevent your application from working correctly.

## Common Causes

- Node version not specified
- Incompatible Node version
- Version not available in build image
- Package requires different version

## How to Fix

### Set Node Version

```toml
[build]
environment = { NODE_VERSION = "18" }
```

### Or package.json

```json
{"engines": {"node": ">=18.0.0"}}
```

