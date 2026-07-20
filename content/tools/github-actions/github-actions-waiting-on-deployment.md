---
title: "[Solution] GitHub Actions Waiting On Deployment"
description: "Fix GitHub Actions deployment waiting status errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Deployment waiting errors occur when the workflow is stuck waiting for approval:

```
Error: Deployment is waiting for environment protection rules
```

## Common Causes

- Required reviewers have not acted on the deployment request.

## How to Fix

**Set deployment timeout:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
- name: Check deployment
  run: |
    gh api repos/{owner}/{repo}/actions/runs/${{ github.run_id }}/deployments | jq '.[].environment'
```
