---
title: "GitHub Actions Secret Not Found"
description: "GitHub Actions workflow fails because a required secret is not configured."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "secret", "governance", "environment", "credential"]
weight: 5
---

# GitHub Actions — Secret Not Found

This error occurs when a workflow references a secret that does not exist or is not accessible in the current environment context. Secrets must be explicitly configured in the repository, organization, or environment settings.

## Common Causes

- Secret name is misspelled
- Secret not configured in repository settings
- Secret belongs to a different environment
- Secret is not available in forks
- Secret is scoped to an environment but not passed

## How to Fix

### Check Secret Name

```yaml
# Wrong
env:
  API_KEY: ${{ secrets.API_KEYY }}  # typo

# Correct
env:
  API_KEY: ${{ secrets.API_KEY }}
```

### Configure Repository Secret

Go to **Settings > Secrets and variables > Actions > New repository secret**

### Use Environment Secrets

```yaml
jobs:
  deploy:
    environment: production
    steps:
      - run: echo ${{ secrets.API_KEY }}
```

### Check Secret Availability

```yaml
- uses: actions/github-script@v7
  with:
    script: |
      if (!process.env.API_KEY) {
        core.setFailed('Secret API_KEY is not set');
      }
```

### Use Default Values for Optional Secrets

```yaml
env:
  API_KEY: ${{ secrets.API_KEY || 'default-key' }}
```

## Examples

```text
Error: Input secret 'API_KEY' not found in the repository's secrets.
```

## Related Errors

- [GitHub Actions Permission Error]({{< relref "/tools/github-actions/github-actions-permission-error" >}}) — permission issues
- [GitHub Actions Env Error]({{< relref "/tools/github-actions/github-actions-env-error" >}}) — environment variable issues
- [GitHub Actions SSH Error]({{< relref "/tools/github-actions/github-actions-ssh-error" >}}) — SSH deploy key issues
