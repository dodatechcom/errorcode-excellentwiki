---
title: "[Solution] GitHub Actions Secret Not Found"
description: "Fix GitHub Actions secret not found errors. Resolve secret configuration and access issues."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "secret", "not-found", "security", "credential"]
weight: 5
---

# GitHub Actions Secret Not Found

A secret not found error occurs when a workflow references a secret that has not been configured in the repository, organization, or environment settings.

## Common Causes

- The secret was never added to the repository settings
- The secret name is misspelled or has incorrect casing
- The secret is in an environment but the environment is not specified in the job
- Forked repository workflows cannot access parent repository secrets

## How to Fix

### Add Secret in Repository Settings

```
Settings > Secrets and variables > Actions > New repository secret
```

### Reference Secrets Correctly

```yaml
steps:
  - run: echo "Using secret"
    env:
      MY_SECRET: ${{ secrets.MY_SECRET }}
```

### Check Secret Spelling

```yaml
# WRONG — case sensitive
${{ secrets.my_secret }}

# CORRECT — must match exactly
${{ secrets.MY_SECRET }}
```

### Use Environment Secrets

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production  # must specify the environment
    steps:
      - run: echo ${{ secrets.PROD_API_KEY }}
```

### Debug with a Safe Check

```yaml
steps:
  - name: Check secret exists
    run: |
      if [ -z "${{ secrets.MY_SECRET }}" ]; then
        echo "::error::Secret MY_SECRET is not set"
        exit 1
      fi
```

## Examples

```yaml
# Secret not configured
deploy:
  steps:
    - run: deploy --key ${{ secrets.DEPLOY_KEY }}
# Error: DEPLOY_KEY is empty
# Fix: add DEPLOY_KEY in repository secrets

# Forked PR cannot access secrets
pull_request_target:
  # Use this event type for fork-safe secret access
  # Be very careful with security
```

## Related Errors

- [Env Error]({{< relref "/tools/github-actions/env-error3" >}}) — environment variable not set
- [Matrix Error]({{< relref "/tools/github-actions/matrix-error" >}}) — matrix configuration issue
