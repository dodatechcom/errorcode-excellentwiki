---
title: "[Solution] Netlify Page Speed Error"
description: "Fix Netlify page speed errors. Resolve issues when site performance metrics are degraded."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Page Speed Error

Fix Netlify page speed errors. Resolve issues when site performance metrics are degraded.

## Common Causes

- Large uncompressed images are served without optimization
- JavaScript bundles are not code-split causing long load times
- Fonts are loaded synchronously blocking the first contentful paint
- Server-side rendering is not used for pages that require fast initial load

## How to Fix

### Check Netlify Configuration

Review your netlify.toml or site settings for misconfigurations.

```toml
# netlify.toml
[build]
  command = "npm run build"
  publish = "dist"
```

### Verify Environment Variables

Ensure all required environment variables are set in the Netlify dashboard.

```bash
# Test locally with netlify dev
npx netlify dev
```

### Check Build Logs

Review the build logs in the Netlify dashboard for specific error messages.

### Clear Build Cache

Trigger a clean build by clearing the Netlify build cache.

## Examples

```toml
# netlify.toml - Example fix
[build]
  command = "npm run build"
  publish = "dist"

[functions]
  directory = "netlify/functions"
```