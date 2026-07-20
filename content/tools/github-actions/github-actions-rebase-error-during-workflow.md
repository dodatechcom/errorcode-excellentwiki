---
title: "[Solution] GitHub Actions Rebase Error During Workflow"
description: "Fix GitHub Actions rebase errors during workflow execution."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Rebase errors occur when a rebase operation in the workflow fails:

```
error: cannot rebase: You have unstaged changes in your working directory
```

## Common Causes

- Uncommitted changes exist before rebase.
- Conflicts during interactive rebase.

## How to Fix

**Stash changes before rebase:**

```yaml
steps:
  - uses: actions/checkout@v4
  - name: Rebase
    run: |
      git config user.name "github-actions"
      git config user.email "github-actions@github.com"
      git fetch origin main
      git rebase origin/main
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
  - name: Rebase
    run: |
      git rebase origin/main || git rebase --abort
```
