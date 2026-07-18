---
title: "[Solution] Netlify Deploy Preview Not Generated Error — How to Fix"
description: "Fix Netlify deploy preview not generated errors. Resolve missing preview deployments, build failures, and PR integration issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Netlify deploy preview not generated error occurs when a pull request or merge request does not trigger a deploy preview deployment. This prevents reviewers from seeing a live preview of changes before merging.

## What This Error Means

Netlify automatically creates deploy previews when pull requests are opened against your configured production branch. When previews are not generated, the integration between Netlify and your Git provider may be disconnected, or the build may have failed during preview creation.

## Why It Happens

- The Netlify GitHub/GitLab/Bitbucket integration is disconnected
- The production branch name in Netlify settings does not match the repository
- The build fails during the deploy preview build
- The pull request was opened against a branch that is not the production branch
- Deploy preview feature is disabled in the site settings
- The Netlify bot does not have permission to comment on the PR
- The build command fails for the preview environment
- The Git provider API rate limit was exceeded

## Common Error Messages

- `No deploy preview available` — Preview was not created for this PR
- `Deploy preview failed` — Build failed during preview creation
- `Build cancelled` — The build was cancelled before completion
- `GitHub integration not configured` — Git provider integration is disconnected

## How to Fix It

### Verify Git Integration

```bash
# Check integration status via API
curl -X GET "https://api.netlify.com/api/v1/sites/SITE_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" | jq '.repo'

# Expected output:
# {
#   "provider": "github",
#   "repo": "owner/repo",
#   "branch": "main",
#   "private": false
# }
```

### Check Deploy Preview Settings

```toml
# netlify.toml — configure deploy preview behavior
[build]
  command = "npm run build"
  publish = "dist"

# Deploy previews use the same build settings as production
# Unless overridden:
[context.deploy-preview]
  command = "npm run build:preview"
  environment = { NODE_ENV = "staging" }

# Branch deploys for non-production branches
[context.branch-deploy]
  command = "npm run build:dev"
```

### Fix PR Comment Integration

```bash
# In Netlify Dashboard:
# Site Settings > Build & Deploy > Deploy Previews
# Enable: "Deploy preview comments on pull requests"

# If the Netlify bot cannot comment:
# 1. Check GitHub repository settings > Integrations
# 2. Ensure Netlify has "Pull requests" permission
# 3. Reinstall the Netlify GitHub App if needed
```

### Trigger Deploy Preview Manually

```bash
# Trigger a deploy preview via API
curl -X POST "https://api.netlify.com/api/v1/sites/SITE_ID/deploys" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "branch": "feature-branch",
    "deploy_trigger": "manual"
  }'

# Or trigger via CLI
netlify deploy --branch=feature-branch
```

### Debug Failed Preview Builds

```bash
# Check deploy preview logs
curl -X GET "https://api.netlify.com/api/v1/sites/SITE_ID/deploys?branch=feature-branch&per_page=5" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" | jq '.[] | {id, state, error_message}'

# Common failure states:
# "error" — Build failed
# "building" — Build in progress
# "waiting" — Build queued

# Check build logs for specific errors
curl -X GET "https://api.netlify.com/api/v1/deploys/DEPLOY_ID/logs" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Configure Preview-Specific Settings

```toml
# netlify.toml — preview-specific configuration
[context.deploy-preview]
  command = "npm run build:preview"
  environment = { NODE_ENV = "staging", DEBUG = "true" }
  publish = "dist"

# For branch deploys
[context.branch-deploy]
  command = "npm run build:dev"
  environment = { NODE_ENV = "development" }
```

### Monitor Deploy Preview Status

```bash
# List recent deploy previews
curl -X GET "https://api.netlify.com/api/v1/sites/SITE_ID/deploys?per_page=10" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" | jq '.[] | {id, state, branch, deploy_url}'

# Check a specific deploy preview
curl -X GET "https://api.netlify.com/api/v1/deploys/DEPLOY_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" | jq '{state, error_message, deploy_url}'
```

### Handle Deploy Preview Cleanup

```bash
# Old deploy previews can accumulate and waste resources
# Clean up old previews via API

# List deploys older than 30 days
curl -X GET "https://api.netlify.com/api/v1/sites/SITE_ID/deploys?per_page=100" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" | jq '.[] | select(.created_at < (now - 2592000)) | .id'

# Delete a specific deploy
curl -X DELETE "https://api.netlify.com/api/v1/deploys/DEPLOY_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Common Scenarios

- **Integration disconnected:** After changing GitHub repository permissions, the Netlify integration was revoked and needs to be reconnected.
- **Wrong branch name:** Netlify is configured to create previews for `master` but the repository uses `main` as the default branch.
- **Build error in preview:** The preview build uses different environment variables (missing a Preview-specific variable) and fails.

## Prevent It

1. Ensure the Netlify GitHub/GitLab integration has all required permissions (read code, write statuses, write PR comments)
2. Verify the production branch name in Netlify settings matches the actual branch name exactly
3. Set up preview-specific environment variables in the `[context.deploy-preview]` section of `netlify.toml`

## Related Pages

- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) — Deployment failed
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) — Build process failed
