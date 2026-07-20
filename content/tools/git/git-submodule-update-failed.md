---
title: "[Solution] Git submodule update failed"
description: "Fix 'git submodule update failed' error. Resolve issues when updating Git submodules to their committed versions."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git submodule update failed

fatal: Needed a single revision
Unable to find current origin/main revision in submodule path '<path>'

This error occurs when `git submodule update` cannot find the expected commit in the submodule's remote repository.

## Common Causes

- Submodule commit not pushed to remote
- Remote URL for submodule has changed
- Submodule commit was force-pushed or rewritten
- Network issues accessing submodule repository
- Submodule path is not properly initialized

## How to Fix

### Initialize Submodules

```bash
git submodule init
git submodule update
```

### Update with Remote

```bash
git submodule update --remote
```

### Synchronize Submodule URLs

```bash
git submodule sync
git submodule update --init --recursive
```

### Manually Check Out Submodule

```bash
cd <submodule-path>
git fetch origin
git checkout <commit-hash>
```

## Examples

```bash
# Example 1: Init and update
git submodule init
git submodule update --recursive

# Example 2: Sync URLs after remote change
git submodule sync --recursive
git submodule update --init --recursive

# Example 3: Manual checkout
cd lib/mysubmodule
git fetch origin
git checkout main
git pull
cd ../..
git add lib/mysubmodule
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
