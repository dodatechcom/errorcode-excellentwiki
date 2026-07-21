---
title: "[Solution] Netlify Cron Function Error"
description: "Fix Netlify cron function errors. Resolve issues when scheduled functions do not execute."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Cron Function Error

Fix Netlify cron function errors. Resolve issues when scheduled functions do not execute.

## Common Causes

- Cron schedule expression in netlify.toml is not in valid syntax
- Cron function is not in the functions directory referenced by the config
- Function is not deployed to production where cron triggers are active
- Cron schedule uses a timezone that does not match the intended execution time

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