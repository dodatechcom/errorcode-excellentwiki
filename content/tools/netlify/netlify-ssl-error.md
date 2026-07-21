---
title: "[Solution] Netlify SSL Error"
description: "Fix Netlify SSL errors. Resolve issues when SSL certificates fail or are not provisioned."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify SSL Error

Fix Netlify SSL errors. Resolve issues when SSL certificates fail or are not provisioned.

## Common Causes

- Custom SSL certificate is uploaded in the wrong format or is invalid
- Domain verification has not completed before SSL provisioning
- Certificate renewal failed because DNS is pointing elsewhere
- SSL certificate does not cover all the subdomains configured for the site

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