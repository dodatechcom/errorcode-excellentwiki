---
title: "[Solution] Workflow Secrets Context Invalid Error"
description: "Fix GitHub Actions secrets context invalid errors when accessing secrets."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Secrets context errors occur when secrets are accessed incorrectly or in unauthorized contexts:

```
Error: secrets context is not available here
```

## Common Causes

- Accessing `secrets` in the `on` trigger (not supported).
- Secret name contains invalid characters.
- Secret not set in the repository or organization settings.

## How to Fix

**Access secrets only in steps:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        run: echo "Deploying with token"
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

**Set the secret via CLI:**

```bash
gh secret set DEPLOY_TOKEN --body "your-token-here"
```

## Examples

```yaml
# Wrong - secrets not available in on trigger
on:
  push:
    branches: [secrets.BRANCH]

# Correct - secrets in steps
steps:
  - run: echo ${{ secrets.API_KEY }}
    env:
      API_KEY: ${{ secrets.API_KEY }}
```
