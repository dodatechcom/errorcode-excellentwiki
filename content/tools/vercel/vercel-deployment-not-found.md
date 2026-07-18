---
title: "[Solution] Vercel Deployment Not Found or Expired Error — How to Fix"
description: "Fix Vercel deployment not found errors. Resolve expired deployments, missing URLs, and production alias configuration issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Vercel deployment not found or expired error occurs when you try to access a deployment URL that no longer exists or has been automatically cleaned up by Vercel's retention policies. This commonly breaks CI/CD pipelines and shared preview links.

## What This Error Means

Vercel retains deployments for a limited time based on your plan. After expiration, deployments are automatically deleted and their URLs return 404 or a "deployment not found" message. Preview deployments for deleted branches may also be removed. Each deployment has a unique URL that becomes invalid once the deployment is purged.

## Why It Happens

- The deployment has expired (older than retention period)
- The deployment was manually deleted
- The branch associated with a preview deployment was deleted
- The project was deleted or transferred to another team
- You are accessing a deployment URL that was never created
- The deployment ID in the URL is incorrect or has a typo
- The deployment failed during build and was never completed
- The deployment was marked as a 404 page and was cleaned up

## Common Error Messages

- `Deployment not found` — The deployment does not exist
- `This deployment has been deleted` — Deployment was removed
- `404: NOT_FOUND` — The URL cannot be resolved to a deployment
- `DEPLOYMENT_NOT_FOUND` — API returns this error code
- `The deployment you are looking for does not exist` — Invalid deployment ID

## How to Fix It

### Check Deployment Status

```bash
# List all deployments for a project
vercel ls --project=your-project-name

# Check a specific deployment
vercel inspect your-deployment-url.vercel.app

# List deployments via API
curl -X GET "https://api.vercel.com/v6/deployments?projectId=YOUR_PROJECT_ID&limit=20" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Recover a Deleted Deployment

```bash
# If the deployment was deleted but the code still exists in git
# Redeploy from the same commit

# Find the commit hash in your git log
git log --oneline -10

# Deploy from that commit
vercel deploy --prod abc1234
```

### Protect Critical Deployments

```bash
# Use Vercel's deployment protection to prevent accidental deletion
# In the dashboard: Settings > Deployment Protection

# Or pin important deployments via API
curl -X POST "https://api.vercel.com/v13/deployments/DEPLOYMENT_ID" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"target": "production"}'
```

### Fix Broken Preview URLs

```bash
# When a branch is deleted, its preview deployment is eventually removed
# To keep preview URLs alive, do not delete branches until ready

# Instead of deleting, merge the branch
git checkout main
git merge feature-branch
git push origin main
git push origin --delete feature-branch
# The preview URL remains accessible briefly after merge

# Or use Vercel's comment integration to track deployment URLs
# before they expire
```

### Create Permanent URLs with Domains

```bash
# Instead of relying on deployment URLs, use custom domains
vercel domains add your-domain.com

# Or use project aliases
vercel alias your-deployment-url.vercel.app stable.your-domain.com
```

### List Active Deployments

```bash
# Check which deployments are still active
curl -X GET "https://api.vercel.com/v6/deployments?projectId=PROJECT_ID&state=READY" \
  -H "Authorization: Bearer YOUR_TOKEN" | jq '.deployments[] | {uid, url, created}'

# Find the latest production deployment
curl -X GET "https://api.vercel.com/v13/deployments?projectId=PROJECT_ID&target=production&limit=1" \
  -H "Authorization: Bearer YOUR_TOKEN" | jq '.deployments[0].url'
```

### Set Up Deployment Retention

```json
// vercel.json — configure retention for important deployments
{
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static"
    }
  ]
}
```

```bash
# In Vercel Dashboard: Settings > General > Deployment Retention
# Configure how long deployments are kept:
# - Hobby: 90 days
# - Pro: 90 days (configurable)
# - Enterprise: Custom

# For preview deployments, you can extend retention per-branch
# Settings > Git > Production Branch > Include Deployment URL
```

### Use Aliases for Stable References

```bash
# Create an alias that always points to the latest production deploy
vercel alias your-project.vercel.app production.your-domain.com

# Aliases are permanent and survive deployment deletions
# They automatically update when new production deployments are made
```

### Set Up Deployment Notifications

```bash
# In Vercel Dashboard: Settings > Notifications
# Configure notifications for:
# - Deployment created
# - Deployment ready
# - Deployment failed
# This helps catch missing deployments early

# Use webhooks for CI/CD integration
curl -X POST "https://api.vercel.com/v1/integrations/deploy/HOOK_ID" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"name": "deploy-ready", "url": "https://your-project.vercel.app"}'
```

## Common Scenarios

- **CI/CD pipeline uses old deployment URL:** A pipeline references a preview deployment URL that has expired, causing integration tests to fail. The pipeline should reference the project's alias URL instead.
- **Shared stakeholder link expired:** You shared a preview URL with a client but it expired before they reviewed it. Use a custom domain alias for important reviews.
- **Branch deleted too early:** A feature branch was deleted after merge, causing its preview deployment to be removed before the team finished reviewing it.

## Prevent It

1. Set up a custom staging domain (e.g., `staging.your-domain.com`) that always points to the latest production deployment
2. Configure Vercel's retention settings to keep preview deployments longer for important branches
3. Never hardcode deployment URLs in CI/CD pipelines — use project aliases or domain-based references instead

## Related Pages

- [Vercel Deploy Error]({{< relref "/tools/vercel/vercel-deploy-error" >}}) — Deployment failed
- [Vercel Domain Error]({{< relref "/tools/vercel/vercel-domain-error" >}}) — Domain verification failed
