---
title: "GitHub Actions GITHUB_TOKEN Permission Error"
description: "GitHub Actions workflow fails due to GITHUB_TOKEN permission issues."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions — GITHUB_TOKEN Permission Error

This error occurs when the `GITHUB_TOKEN` does not have sufficient permissions to perform an operation in the workflow. The token may lack write access, or the workflow's permission scope may be too restrictive.

## Common Causes

- Workflow `permissions` block too restrictive
- Repository settings restrict token permissions
- Token scope does not cover the required action
- Organization policy limits token permissions

## How to Fix

### Set Workflow Permissions

```yaml
permissions:
  contents: write
  pull-requests: write
  issues: write
```

### Use Minimal Required Permissions

```yaml
jobs:
  build:
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4
```

### Grant Write Access for Deployment

```yaml
permissions:
  contents: write
  pages: write
  id-token: write
```

### Check Repository Settings

Go to **Settings > Actions > General > Workflow permissions** and ensure "Read and write permissions" is selected.

### Use Custom Token for External Operations

```yaml
steps:
  - uses: actions/github-script@v7
    with:
      github-token: ${{ secrets.CUSTOM_TOKEN }}
```

### Debug Token Permissions

```yaml
- uses: actions/github-script@v7
  with:
    script: |
      console.log(context.repo);
      console.log(context.payload);
```

## Examples

```text
remote: Permission to org/repo.git denied to github-actions[bot].
fatal: unable to access 'https://github.com/org/repo.git/':
  The requested URL returned error: 403
```

## Related Errors

- [GitHub Actions Secret Error]({{< relref "/tools/github-actions/github-actions-secret-error" >}}) — secret not found
- [GitHub Actions YAML Error]({{< relref "/tools/github-actions/github-actions-yaml-error" >}}) — YAML syntax error
- [GitHub Actions SSH Error]({{< relref "/tools/github-actions/github-actions-ssh-error" >}}) — SSH deploy key issues
