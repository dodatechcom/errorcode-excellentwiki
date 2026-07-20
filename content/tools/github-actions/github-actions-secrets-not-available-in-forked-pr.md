---
title: "[Solution] GitHub Actions Secrets Not Available In Forked PR"
description: "Fix GitHub Actions secrets not available in forked PR workflows."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Secrets are not available in workflows triggered by forked PRs:

```
Error: The secret 'DEPLOY_TOKEN' is not available
Forked workflows do not have access to repository secrets
```

## Common Causes

- Security feature: secrets are not exposed to forked PRs.
- Workflow expects secrets but trigger is a pull_request from a fork.

## How to Fix

**Use pull_request_target for fork PRs:**

```yaml
on:
  pull_request_target:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}
```

## Examples

```yaml
steps:
  - name: Check secrets
    id: check
    run: |
      if [ -n "${{ secrets.DEPLOY_TOKEN }}" ]; then
        echo "has_secret=true" >> $GITHUB_OUTPUT
      else
        echo "has_secret=false" >> $GITHUB_OUTPUT
      fi
```
