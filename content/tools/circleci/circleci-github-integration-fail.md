---
title: "[Solution] CircleCI GitHub Integration Fail"
description: "Fix CircleCI GitHub integration failures when the pipeline cannot report status or access repository resources."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI GitHub Integration Fail

GitHub integration failures occur when CircleCI cannot report build status, access repository metadata, or respond to GitHub webhook events.

## Common Causes

- GitHub OAuth token expired or was revoked
- CircleCI GitHub App permissions were modified
- Repository was transferred to a different organization
- GitHub API rate limiting blocks status updates
- Webhook configuration was corrupted

## How to Fix

### Solution 1: Re-authorize the GitHub integration

Navigate to **CircleCI > Project Settings > Integrations** and re-authorize the GitHub connection.

### Solution 2: Check webhook status

```bash
# List webhooks for the repository
curl -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/owner/repo/hooks"
```

### Solution 3: Manually trigger a pipeline

```bash
# Trigger pipeline via CircleCI API
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"branch":"main"}' \
  "https://circleci.com/api/v2/project/gh/owner/repo/pipeline"
```

## Examples

```
Error: GitHub status check could not be created
Webhook delivery failed: connection refused
```

## Prevent It

- Monitor CircleCI integration health regularly
- Keep GitHub App permissions up to date
- Re-authorize after organization changes
