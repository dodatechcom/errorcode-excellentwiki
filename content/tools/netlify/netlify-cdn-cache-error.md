---
title: "[Solution] Netlify CDN Cache Error"
description: "Fix Netlify CDN cache errors. Resolve issues when cached content is stale or not purged."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify CDN Cache Error

Fix Netlify CDN cache errors. Resolve issues when cached content is stale or not purged.

## Common Causes

- Cache headers are set to cache everything including dynamic content
- Manual cache purge was not triggered after a new deployment
- Edge server has not yet propagated the cache invalidation command
- Cache control directives conflict between the build output and Netlify defaults

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