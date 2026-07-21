---
title: "[Solution] Vercel Git Integration Error"
description: "Fix Vercel Git integration errors when GitHub, GitLab, or Bitbucket connections fail."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Git Integration Error

Vercel Git integration fails to connect or sync with repositories.

```
Error: Git repository not found
```

## Common Causes

- Repository permissions revoked
- Organization access not granted
- Webhook deleted or expired
- Repository moved or renamed
- GitHub App installation incomplete

## How to Fix

### Reconnect Repository

```bash
# Via Dashboard
# Project Settings > Git > Repository
# Click "Reconnect" or re-select repository
```

### Check Permissions

```bash
# Ensure Vercel app has access:
# - Read access to code
# - Write access to deployments
# - Access to pull requests
```

### Update Git Integration

```bash
# Via CLI
vercel git connect

# Check connected repos
vercel git list
```

### Fix Webhook Issues

```bash
# Check webhook status in GitHub
# Settings > Webhooks > Look for Vercel webhook
# Ensure it's active and last delivery succeeded
```

### Reinstall Vercel App

```
1. Go to GitHub Settings > Applications > Installed Apps
2. Find Vercel
3. Uninstall
4. Reinstall from Vercel Dashboard
```

### Verify Branch Configuration

```bash
# Check production branch
vercel project ls

# Set production branch
vercel project link --prod
```

## Examples

```bash
# Force redeploy after fixing integration
vercel --force

# Check deployment status
vercel deployment ls

# View project settings
vercel project ls
```
