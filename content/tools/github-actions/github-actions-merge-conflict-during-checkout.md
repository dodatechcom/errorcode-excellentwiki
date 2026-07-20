---
title: "[Solution] GitHub Actions Merge Conflict During Checkout"
description: "Fix GitHub Actions merge conflict errors during checkout in CI."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Merge conflict errors occur when automatic merge during checkout fails:

```
error: Your local changes to the following files would be overwritten
Merge failed; fix conflicts and then commit the result.
```

## Common Causes

- Concurrent workflow runs modifying the same branch.
- Auto-merge feature attempted to merge conflicting changes.

## How to Fix

**Check for conflicts before running:**

```bash
git fetch origin main
git merge --no-commit --no-ff origin/main || {
  echo "Merge conflict detected"
  exit 1
}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
  - name: Check for merge conflicts
    run: |
      git fetch origin ${{ github.base_ref }}
      git merge-tree $(git merge-base HEAD origin/${{ github.base_ref }}) HEAD origin/${{ github.base_ref }}
```
