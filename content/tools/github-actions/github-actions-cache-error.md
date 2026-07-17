---
title: "GitHub Actions Cache Error"
description: "GitHub Actions cache operation fails during workflow execution."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "cache", "speed-up", "dependencies", "artifacts"]
weight: 5
---

# GitHub Actions Cache Error

A GitHub Actions cache error occurs when the `actions/cache` action fails to save, restore, or access cached dependencies and build artifacts.

## Common Causes

- Cache key does not match any existing cache
- Cache size exceeds GitHub's 10GB limit per repository
- Cache permissions issue
- Cache is from a different branch or workflow

## How to Fix

### Use Proper Cache Key

```yaml
- name: Cache node modules
  uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

### Cache Multiple Paths

```yaml
- name: Cache dependencies
  uses: actions/cache@v4
  with:
    path: |
      ~/.npm
      node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

### Check Cache Usage

```bash
gh cache list --repo owner/repo
```

### Delete Old Caches

```bash
gh cache delete --repo owner/repo --all
```

### Fix Cache Permissions

```yaml
# Ensure workflow has cache permissions
permissions:
  actions: read/write
```

### Use Cache with Restore Only

```yaml
- name: Restore cache
  uses: actions/cache/restore@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

## Examples

```yaml
# Cache miss - not an error, just slow
Cache not found for key: Linux-node-abc123

# Cache error
Error: Unable to find any cache key matching pattern: ...
```

## Related Errors

- [Artifact Error]({{< relref "/tools/github-actions/github-actions-artifact-error" >}}) — artifact upload error
- [Timeout Error]({{< relref "/tools/github-actions/github-actions-timeout-error" >}}) — job timeout
