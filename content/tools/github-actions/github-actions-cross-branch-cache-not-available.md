---
title: "[Solution] GitHub Actions Cross-Branch Cache Not Available"
description: "Fix GitHub Actions cross-branch cache scope limitations."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cross-branch cache limitations prevent workflows from accessing caches from other branches:

```
Warning: Cache not found for key from branch: feature-x
```

## Common Causes

- Default cache scope is limited to the current branch.
- PR from a fork cannot access the base branch cache.

## How to Fix

**Use cache from the default branch:**

```yaml
env:
  CACHE_KEY_PREFIX: ${{ github.ref == 'refs/heads/main' && 'main' || 'pr' }}
steps:
  - uses: actions/cache@v4
    with:
      path: node_modules
      key: ${{ runner.os }}-npm-${{ env.CACHE_KEY_PREFIX }}-${{ hashFiles('**/package-lock.json') }}
      restore-keys: |
        ${{ runner.os }}-npm-main-
```

## Examples

```yaml
# Use base branch for PRs
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-${{ github.base_ref }}-
```
