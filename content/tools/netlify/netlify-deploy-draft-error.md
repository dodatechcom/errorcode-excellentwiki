---
title: "[Solution] Netlify Deploy Draft Error"
description: "Fix Netlify deploy draft errors. Resolve issues when draft deploys are not published."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Deploy Draft Error

Fix Netlify deploy draft errors. Resolve issues when draft deploys are not published.

## Common Causes

- Draft deploy is created but the publish button was not clicked
- Draft deploy build output does not pass the deploy validation checks
- Draft deploy is hidden because branch deploy rules filter it out
- Draft deploy preview URL is not generated because of a build timeout

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