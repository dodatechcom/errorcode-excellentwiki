---
title: "[Solution] Netlify Headers Security Error"
description: "Fix Netlify security headers errors. Resolve issues when security headers block resource loading."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Headers Security Error

Fix Netlify security headers errors. Resolve issues when security headers block resource loading.

## Common Causes

- Content Security Policy header blocks scripts from allowed domains
- Strict Transport Security header forces HTTPS on a domain without a cert
- X-Frame-Options header prevents embedding in an iframe that is required
- Referrer Policy header is too strict for cross-origin resource sharing

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