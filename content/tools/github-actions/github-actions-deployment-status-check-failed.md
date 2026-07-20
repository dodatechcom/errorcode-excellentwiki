---
title: "[Solution] GitHub Actions Deployment Status Check Failed"
description: "Fix GitHub Actions deployment status check failures."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Deployment status check errors occur when status checks fail during deployment:

```
Error: Required status check 'deploy/production' is not successful
```

## Common Causes

- Required status check was not triggered.
- Deployment workflow failed.

## How to Fix

**Ensure deployment job has correct name:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - run: deploy.sh
```

## Examples

```yaml
# Configure branch protection with status checks
# Settings > Branches > Branch protection rules > Require status checks
```
