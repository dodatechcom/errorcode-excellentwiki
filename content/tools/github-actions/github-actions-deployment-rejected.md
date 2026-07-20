---
title: "[Solution] GitHub Actions Deployment Rejected"
description: "Fix GitHub Actions deployment rejected by environment protection."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Deployment rejected errors occur when the environment protection rules reject the deployment:

```
Error: Deployment rejected by required reviewer
```

## Common Causes

- Reviewer explicitly rejected the deployment.
- Deployment does not meet required criteria.

## How to Fix

**Re-run the deployment:**

```yaml
steps:
  - name: Report status
    if: failure()
    run: |
      gh pr comment ${{ github.event.pull_request.number }}         --body "Deployment was rejected. Please review environment protection rules."
```

## Examples

```yaml
steps:
  - name: Retry deployment
    run: |
      gh api repos/{owner}/{repo}/actions/runs/${{ github.run_id }}/deployment-faults
```
