---
title: "[Solution] GitHub Actions Environment Variable Not Set"
description: "Fix GitHub Actions environment variable errors. Resolve undefined and missing env variable issues."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions Environment Variable Not Set

This error occurs when a workflow step references an environment variable that is not defined in the workflow, repository settings, or environment configuration.

## Common Causes

- The `env` key is missing from the workflow file
- A repository or environment secret is not configured in GitHub settings
- A variable name is misspelled or has incorrect casing
- The variable is set at a different scope (job vs step level)

## How to Fix

### Define Environment Variables in the Workflow

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      NODE_ENV: production
    steps:
      - run: echo "Building in $NODE_ENV mode"
```

### Set Variables from Previous Steps

```yaml
steps:
  - id: set-var
    run: echo "MY_VAR=hello" >> $GITHUB_OUTPUT
  - run: echo "${{ steps.set-var.outputs.MY_VAR }}"
```

### Reference Secrets Properly

```yaml
steps:
  - run: echo "Deploying..."
    env:
      API_KEY: ${{ secrets.API_KEY }}
```

### Check Secret Exists in Repository Settings

```
Settings > Secrets and variables > Actions > Repository secrets
```

### Use Default Values for Optional Variables

```yaml
steps:
  - run: echo "Branch is ${BRANCH_NAME:-main}"
    env:
      BRANCH_NAME: ${{ github.head_ref || 'main' }}
```

## Examples

```yaml
# Secret not configured
- run: deploy --token ${{ secrets.DEPLOY_TOKEN }}
# Error: empty string — secret DEPLOY_TOKEN not found
# Fix: add DEPLOY_TOKEN in repository secrets

# Variable at wrong scope
env:
  MY_VAR: hello
steps:
  - run: echo ${{ steps.my-step.outputs.MY_VAR }}
  # MY_VAR is not a step output — use job env instead
```

## Related Errors

- [Secret Error]({{< relref "/tools/github-actions/secret-error" >}}) — secret not found
- [Step Failed]({{< relref "/tools/github-actions/step-failed" >}}) — step execution failure
