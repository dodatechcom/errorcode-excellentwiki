---
title: "GitHub Actions Environment Variable Not Set"
description: "GitHub Actions workflow fails because an environment variable is not set."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions — Environment Variable Not Set

This error occurs when a GitHub Actions workflow references an environment variable that is not set. The variable may be missing from the workflow, repository, or environment configuration.

## Common Causes

- Environment variable not defined in workflow
- Variable defined at wrong scope
- Variable not available in forked repository
- Variable name is misspelled
- Variable not set in environment

## How to Fix

### Define Environment Variable in Workflow

```yaml
env:
  NODE_ENV: production
  API_URL: https://api.example.com

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo $API_URL
```

### Set Variable at Job Level

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      BUILD_ENV: production
    steps:
      - run: echo $BUILD_ENV
```

### Set Variable at Step Level

```yaml
steps:
  - name: Build
    env:
      NODE_OPTIONS: '--max-old-space-size=4096'
    run: npm run build
```

### Use Default Values

```yaml
env:
  API_KEY: ${{ secrets.API_KEY || 'default-key' }}
```

### Check Built-in Variables

```yaml
- run: |
    echo "Branch: $GITHUB_REF"
    echo "SHA: $GITHUB_SHA"
    echo "Actor: $GITHUB_ACTOR"
```

## Examples

```text
Error: API_URL: unbound variable
```

## Related Errors

- [GitHub Actions Secret Error]({{< relref "/tools/github-actions/github-actions-secret-error" >}}) — secret not found
- [GitHub Actions YAML Error]({{< relref "/tools/github-actions/github-actions-yaml-error" >}}) — YAML syntax error
- [GitHub Actions Env Error]({{< relref "/tools/github-actions/github-actions-env-error" >}}) — environment issues
