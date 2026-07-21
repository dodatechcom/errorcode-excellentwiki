---
title: "[Solution] Vercel ISR Error Pages Error"
description: "Fix Vercel ISR error pages errors. Resolve issues when error pages are cached incorrectly."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel ISR Error Pages Error

Fix Vercel ISR error pages errors. Resolve issues when error pages are cached incorrectly.

## Common Causes

- Error page is cached by ISR but the error state should not be cached
- Revalidation of the error page is blocked because the page is not ISR enabled
- Error boundary catches the error but still generates a cached 500 response
- ISR cache stores the error response before the server can recover

## How to Fix

### Check vercel.json Configuration

Review your Vercel configuration for misconfigurations.

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "framework": "nextjs"
}
```

### Verify Environment Variables

Check that all required environment variables are set in the Vercel project settings.

```bash
# List environment variables
vercel env ls
```

### Check Deployment Logs

Review the deployment logs in the Vercel dashboard or via the CLI.

```bash
vercel logs
```

### Redeploy

Trigger a fresh deployment to resolve transient issues.

```bash
vercel --prod
```

## Examples

```json
// vercel.json - Example fix
{
  "routes": [{
    "src": "/api/(.*)",
    "dest": "/api/$1"
  }]
}
```