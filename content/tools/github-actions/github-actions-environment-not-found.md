---
title: "[Solution] GitHub Actions Environment Not Found"
description: "Fix GitHub Actions environment not found errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Environment not found errors occur when the workflow references a non-existent environment:

```
Error: Environment 'staging' not found in repository
```

## Common Causes

- Environment was not created in repository settings.
- Typo in environment name.

## How to Fix

**Create the environment:**

```bash
gh api repos/{owner}/{repo}/environments -f name=staging
```

## Examples

```yaml
jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment: staging
  deploy-production:
    runs-on: ubuntu-latest
    environment: production
    needs: deploy-staging
```
