---
title: "[Solution] GitHub Actions Context Error Accessing Secrets"
description: "Fix GitHub Actions context errors when accessing secrets in expressions."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Context errors occur when secrets are referenced incorrectly:

```
Error: Invalid context access: 'secrets.UNDEFINED_SECRET'
```

## Common Causes

- Secret name does not exist in the repository.
- Typo in secret name (case-sensitive).

## How to Fix

**Verify the secret exists:**

```bash
gh secret list
```

**Use correct context syntax:**

```yaml
steps:
  - name: Deploy
    env:
      API_KEY: ${{ secrets.API_KEY }}
    run: echo "Using API key"
```

## Examples

```yaml
env:
  MY_SECRET: ${{ secrets.MY_SECRET }}
```
