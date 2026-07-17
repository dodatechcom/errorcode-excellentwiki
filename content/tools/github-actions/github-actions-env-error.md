---
title: "GitHub Actions Environment Variable Error"
description: "GitHub Actions workflow fails due to environment variable configuration issues."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "environment", "variable", "env", "context"]
weight: 5
---

# GitHub Actions Environment Variable Error

An environment variable error occurs when GitHub Actions cannot access, set, or reference environment variables correctly in the workflow. This can cause steps to fail with missing or incorrect values.

## Common Causes

- Environment variable not defined in workflow or repository
- Incorrect variable reference syntax (`$VAR` vs `${{ vars.VAR }}`)
- Variable name mismatch (case sensitivity)
- Environment not properly configured

## How to Fix

### Set Environment Variables in Workflow

```yaml
env:
  NODE_ENV: production
  API_URL: https://api.example.com

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      JOB_VAR: job-value
    steps:
      - run: echo $NODE_ENV $API_URL
```

### Use Repository Variables

```yaml
- run: echo ${{ vars.MY_VARIABLE }}
```

### Use Secrets Properly

```yaml
- run: echo ${{ secrets.MY_SECRET }}
```

### Set Per-Step Environment

```yaml
steps:
  - name: Build
    run: npm run build
    env:
      NODE_ENV: production
      API_KEY: ${{ secrets.API_KEY }}
```

### Fix Variable References

```yaml
# Correct
- run: echo "Hello ${{ github.actor }}"

# Wrong
- run: echo "Hello $github.actor"  # Missing ${{ }}
```

### Check Environment Configuration

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
```

## Examples

```yaml
# Error: variable not found
- run: echo ${{ vars.MISSING_VAR }}
# Warning: Context access invalid

# Fix: add variable in repository settings
# Settings > Secrets and variables > Actions > Variables
```

## Related Errors

- [Secret Error]({{< relref "/tools/github-actions/github-actions-secret-error" >}}) — secret not found
- [Permission Error]({{< relref "/tools/github-actions/github-actions-permission-error" >}}) — permission issues
