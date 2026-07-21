---
title: "[Solution] Vercel Project Link Error"
description: "Fix Vercel project link errors. Resolve issues when the CLI cannot link to a project."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Project Link Error

Fix Vercel project link errors. Resolve issues when the CLI cannot link to a project.

## Common Causes

- Vercel CLI is not authenticated with a valid team or user token
- Project name in the link configuration does not match the dashboard
- Git repository origin does not match the linked Vercel project
- Project link was created in a directory that is not the project root

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