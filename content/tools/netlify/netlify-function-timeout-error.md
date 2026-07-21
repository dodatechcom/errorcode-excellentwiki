---
title: "[Solution] Netlify Function Timeout Error"
description: "Fix Netlify function timeout errors. Resolve issues when functions exceed the execution time limit."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Function Timeout Error

Fix Netlify function timeout errors. Resolve issues when functions exceed the execution time limit.

## Common Causes

- Function makes an external API call that hangs without a timeout
- Database connection inside the function is slow to establish
- Function is processing a large payload that exceeds processing limits
- Function runtime is set to a version with a lower timeout threshold

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