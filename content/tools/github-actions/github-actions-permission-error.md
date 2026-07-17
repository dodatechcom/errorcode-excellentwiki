---
title: "GitHub Actions Permission Error"
description: "GitHub Actions workflow fails due to insufficient permissions."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions Permission Error

A GitHub Actions permission error occurs when the workflow lacks the necessary permissions to perform an operation. This can affect repository access, deployments, and API calls.

## Common Causes

- Default `GITHUB_TOKEN` permissions too restrictive
- Workflow tries to write to a protected branch
- Repository-level permission settings block the action
- Missing `permissions` declaration in workflow

## How to Fix

### Add Permissions to Workflow

```yaml
# .github/workflows/ci.yml
permissions:
  contents: write
  packages: write
  pull-requests: write
```

### Set Job-Level Permissions

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pages: write
      id-token: write
```

### Check Repository Permission Settings

Go to **Settings > Actions > General > Workflow permissions**:
- Select "Read and write permissions"

### Use Personal Access Token

```yaml
- uses: actions/checkout@v4
  with:
    token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
```

### Fix Deployment Permissions

```yaml
- name: Deploy to GitHub Pages
  uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
```

## Examples

```yaml
# Error: Permission denied
- run: git push origin main
# remote: Permission to repo denied

# Fix: add permissions
permissions:
  contents: write
```

## Related Errors

- [Secret Error]({{< relref "/tools/github-actions/github-actions-secret-error" >}}) — secret not found
- [Workflow Error]({{< relref "/tools/github-actions/workflow-failed" >}}) — workflow failure
