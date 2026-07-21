---
title: "[Solution] Netlify Asset Optimization Error"
description: "Fix Netlify asset optimization errors. Resolve issues when built-in optimization produces wrong results."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Asset Optimization Error

Fix Netlify asset optimization errors. Resolve issues when built-in optimization produces wrong results.

## Common Causes

- Image optimization service generates images with incorrect dimensions
- Minification of HTML strips content that should be preserved
- Asset processing skips files that match the ignore patterns
- Optimization service is down causing builds to hang waiting for response

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