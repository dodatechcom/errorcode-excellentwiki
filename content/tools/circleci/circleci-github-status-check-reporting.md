---
title: "[Solution] CircleCI GitHub Status Check Reporting"
description: "Fix CircleCI GitHub status check reporting errors when build status is not correctly reported back to pull requests."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI GitHub Status Check Reporting

GitHub status check reporting errors occur when CircleCI cannot report the build status back to GitHub, causing pull requests to show no status or incorrect status.

## Common Causes

- CircleCI GitHub App was removed from the repository
- Commit SHA does not match the expected format
- GitHub API rate limiting blocks status updates
- Repository permissions were changed after integration setup
- Pipeline is running on a fork without proper configuration

## How to Fix

### Solution 1: Reconnect the CircleCI GitHub App

Navigate to **GitHub > Settings > Integrations** and verify CircleCI is installed.

### Solution 2: Check repository permissions

```bash
# Verify CircleCI can access the repository
curl -H "Circle-Token: $TOKEN" \
  "https://circleci.com/api/v2/project/gh/owner/repo"
```

### Solution 3: Manually trigger status update

```yaml
jobs:
  notify:
    steps:
      - run:
          name: Report status to GitHub
          command: |
            curl -X POST \
              -H "Authorization: token $GITHUB_TOKEN" \
              -d '{"state":"success","description":"Build passed"}' \
              "https://api.github.com/repos/owner/repo/statuses/$CIRCLE_SHA1"
```

## Examples

```
Error: GitHub status check could not be created: 403
Warning: Status update failed for commit abc123
```

## Prevent It

- Keep the CircleCI GitHub App installed and authorized
- Monitor pipeline status in the CircleCI dashboard
- Re-authorize after repository ownership changes
