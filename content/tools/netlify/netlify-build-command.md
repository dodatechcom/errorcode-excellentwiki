---
title: "[Solution] Netlify Build Command Error"
description: "Fix Netlify build command errors. Resolve build script configuration issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Build Command Error can prevent your application from working correctly.

## Common Causes

- Build command not found
- Command syntax error
- Package.json script missing
- Command not executable

## How to Fix

### Set Build Command

```toml
[build]
command = "npm run build"
```

### Verify Script Exists

```bash
cat package.json | grep scripts
```

