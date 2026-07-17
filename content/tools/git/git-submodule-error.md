---
title: "[Solution] Git Submodule Error — submodule not initialized"
description: "Fix Git submodule not initialized errors. Initialize and update submodules correctly."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A submodule error occurs when Git submodules are not initialized or updated after cloning or pulling a repository. The submodule directories exist but are empty.

## Common Causes

- Cloned a repo without `--recurse-submodules`
- Did not run `git submodule init` and `git submodule update` after clone
- The `.gitmodules` file references a repository that no longer exists
- Submodule URL changed or repository was moved
- Insufficient permissions to access the submodule repository

## How to Fix

### Initialize and Update Submodules

```bash
git submodule init
git submodule update
```

### Clone with Submodules

```bash
git clone --recurse-submodules <repo-url>
```

### Update Submodules to Latest Commits

```bash
git submodule update --remote
```

### Check Submodule Status

```bash
git submodule status
```

### Fix Broken Submodule URL

```bash
git config submodule.<name>.url <new-url>
git submodule update --init --remote
```

## Examples

```bash
# Example 1: Clone with submodules
git clone --recurse-submodules https://github.com/user/repo.git

# Example 2: Fix after clone
git submodule init
git submodule update

# Example 3: Update all submodules to latest
git submodule foreach git pull origin main
```

## Related Errors

- [Git LFS Error]({{< relref "/tools/git/git-lfs-error" >}}) — Git LFS pointer file mismatch
- [Git Submodule Error]({{< relref "/tools/git/git-submodule-error" >}}) — submodule initialization
