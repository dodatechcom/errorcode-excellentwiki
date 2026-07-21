---
title: "[Solution] Netlify Build Cache Error"
description: "Fix Netlify build cache errors when cached dependencies cause build failures or stale artifacts."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Netlify build cache contains stale or corrupted data that causes the build to fail or produce incorrect output.

## Common Causes

- Cached node_modules incompatible with new lock file
- Cache contains outdated build artifacts
- Cache from different Node.js version
- Corrupted cache during previous build
- Cache size exceeds limits

## How to Fix

- Clear the build cache from the Netlify dashboard
- Disable caching temporarily to diagnose
- Use netlify.toml to control cache behavior

## Examples

```toml
# netlify.toml
[build]
  command = "npm run build"
  publish = "dist"

# Disable cache for specific directory
[[plugins]]
  package = "netlify-plugin-cache"
  [plugins.inputs]
    paths = ["node_modules/.cache"]
```

Clear cache via CLI:

```bash
npx netlify-cli build --clear-cache
```
