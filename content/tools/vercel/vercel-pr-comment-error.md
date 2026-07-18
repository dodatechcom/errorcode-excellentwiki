---
title: "[Solution] Vercel PR Comment Error — Fix Preview Deployment Comment Failed"
description: "Fix Vercel PR comment errors when GitHub PR comments with preview deployment URLs fail to post. Resolve GitHub token, permissions, and integration issues."
tools: ["vercel"]
error-types: ["integration-error"]
severities: ["warning"]
weight: 5
---

A Vercel PR comment error occurs when the Vercel GitHub integration cannot post a comment on a pull request with the preview deployment URL. The comment may fail to appear or show an incorrect URL.

## What This Error Means

Vercel automatically comments on GitHub pull requests with preview deployment links. When this fails:

```
Error: Could not create comment on pull request #42
Failed to post deployment status to GitHub
```

## Why It Happens

- The GitHub App installation does not have permission to write to the repository
- The GitHub token is expired or invalid
- The repository is not connected to the Vercel project
- The pull request was created by a fork without write access
- GitHub API rate limits are exceeded
- The Vercel integration is disabled for the repository
- The deployment URL is not ready when the comment is attempted

## How to Fix It

### Check Vercel GitHub Integration

Go to Vercel Dashboard > Git > Connected Repository and verify the integration is active.

### Reinstall the Vercel GitHub App

```bash
# Go to GitHub > Settings > Applications > Vercel
# Remove and reinstall
```

### Check Repository Permissions

Ensure the Vercel GitHub App has read and write access to the repository.

### Manually Post the Comment

```bash
vercel inspect --scope <team> | grep "Preview"
# Copy the preview URL and post manually
```

### Disable Auto-Comment in vercel.json

```json
{
  "github": {
    "silent": true
  }
}
```

### Check GitHub Token

```bash
# In Vercel dashboard, go to Git > Access Token
# Verify the token is valid and has correct permissions
```

### Use a Custom Comment Template

```json
{
  "github": {
    "commentOnPullRequest": true,
    "silent": false
  }
}
```

### Fork PR Workaround

For PRs from forks, provide the preview URL in a separate comment or description.

## Common Mistakes

- Revoking the Vercel GitHub App token without updating Vercel
- Having GitHub rate limits due to excessive API calls
- Not checking the Vercel deployment logs for integration-specific errors
- Assuming PR comments work for cross-fork PRs without additional configuration

## Related Pages

- [Vercel Deploy Error]({{< relref "/tools/vercel/vercel-deploy-error" >}}) -- Deploy failures
- [Vercel Project Error]({{< relref "/tools/vercel/vercel-project-error" >}}) -- Project configuration
- [Vercel Build Error]({{< relref "/tools/vercel/vercel-build-error" >}}) -- Build failures
