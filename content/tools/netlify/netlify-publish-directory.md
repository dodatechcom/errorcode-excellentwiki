---
title: "[Solution] Netlify Publish Directory Error"
description: "Fix Netlify publish directory errors. Resolve build output directory issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Publish Directory Error can prevent your application from working correctly.

## Common Causes

- Directory does not exist
- Wrong directory specified
- Build output in unexpected location

## How to Fix

### Set Publish Directory

```toml
[build]
publish = "dist"
```

### Check Output

```bash
ls -la dist/
```

