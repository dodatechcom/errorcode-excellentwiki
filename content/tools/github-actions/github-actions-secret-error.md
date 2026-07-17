---
title: "GitHub Actions Secret Not Found"
description: "GitHub Actions workflow cannot access a configured secret."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "secret", "environment", "credential", "token"]
weight: 5
---

# GitHub Actions Secret Not Found

A GitHub Actions secret not found error occurs when a workflow references a secret that does not exist, is not accessible, or is not configured in the repository settings.

## Common Causes

- Secret is not configured in repository settings
- Secret name typo in the workflow
- Secret is set at organization level but not available to the repository
- Environment-scoped secret not available in the current environment

## How to Fix

### Check Secret Configuration

Go to **Settings > Secrets and variables > Actions** and verify the secret exists.

### Fix Secret Name in Workflow

```yaml
# Correct (secret names are case-sensitive)
- run: echo ${{ secrets.MY_SECRET }}

# Wrong
- run: echo ${{ secrets.my_secret }}
```

### Set Organization-Level Secrets

```bash
gh secret set MY_SECRET --org my-org --visibility all
```

### Configure Environment Secrets

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: echo ${{ secrets.PROD_SECRET }}
```

### Check Secret Accessibility

```yaml
- name: Debug Secret
  run: |
    if [ -z "${{ secrets.MY_SECRET }}" ]; then
      echo "Secret is empty or not set"
    fi
```

### Use Variables for Non-Sensitive Data

```yaml
# Use variables instead of secrets for non-sensitive config
- run: echo ${{ vars.MY_VARIABLE }}
```

## Examples

```yaml
# Error: Secret not found
- run: deploy --token ${{ secrets.DEPLOY_TOKEN }}
# Error: The secret 'DEPLOY_TOKEN' is not available

# Fix: add secret in repository settings
# Settings > Secrets and variables > Actions > New repository secret
```

## Related Errors

- [Permission Error]({{< relref "/tools/github-actions/github-actions-permission-error" >}}) — permission issues
- [Environment Error]({{< relref "/tools/github-actions/github-actions-env-error" >}}) — environment variable issues
