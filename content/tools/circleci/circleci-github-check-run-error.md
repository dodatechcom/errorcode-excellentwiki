---
title: "[Solution] CircleCI GitHub Check Run Error"
description: "Fix CircleCI GitHub check run errors when the pipeline cannot create or update check runs on pull requests."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI GitHub Check Run Error

GitHub check run errors occur when CircleCI cannot create or update check runs on pull requests, preventing status checks from appearing.

## Common Causes

- GitHub App permissions do not include checks:write
- Repository was archived or permissions were changed
- GitHub API rate limiting blocks the check run update
- Check run name exceeds GitHub's character limit
- GitHub App was removed from the repository

## How to Fix

### Solution 1: Verify GitHub App permissions

Navigate to **GitHub > Settings > Integrations > CircleCI** and ensure the app has:
- Checks: Read & Write
- Pull requests: Read & Write

### Solution 2: Re-install the CircleCI GitHub App

```bash
# Visit CircleCI project settings and reconnect GitHub
```

### Solution 3: Check GitHub API rate limits

```bash
curl -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/rate_limit"
```

## Examples

```
Error: GitHub check run could not be created: 403 Forbidden
Warning: Failed to update check run status
```

## Prevent It

- Keep CircleCI GitHub App permissions up to date
- Monitor GitHub API rate limits during heavy CI usage
- Re-authorize the app after repository ownership changes
