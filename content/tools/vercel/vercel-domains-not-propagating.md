---
title: "[Solution] Vercel Domains Not Propagating"
description: "Fix Vercel domain propagation errors. Resolve issues when domains take too long to become active."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Domains Not Propagating

Fix Vercel domain propagation errors. Resolve issues when domains take too long to become active.

## Common Causes

- DNS changes have not fully propagated across the global DNS servers
- Domain registrar has a long TTL that delays the update
- Nameserver records are pointing to the wrong Vercel nameservers
- Domain verification has not completed in the Vercel dashboard

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