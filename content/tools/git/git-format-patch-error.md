---
title: "[Solution] Git format-patch error"
description: "Fix 'git format-patch' error. Resolve issues when creating patch files from commits for email or sharing."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git format-patch error

fatal: <commit> does not have any commits

This error occurs when the revision range specified for `git format-patch` does not produce any patches.

## Common Causes

- No commits in the specified range
- Wrong revision range specified
- Branch is up to date with the base
- Empty range or invalid commit references

## How to Fix

### Check Commit Range

```bash
git log --oneline origin/main..HEAD
```

### Use Correct Range

```bash
git format-patch origin/main
```

### Create Patches from Last N Commits

```bash
git format-patch -3
```

### Output to Directory

```bash
git format-patch -o patches/ origin/main
```

## Examples

```bash
# Example 1: No commits since fork
git format-patch origin/main
# No output (no commits to patch)
# Fix: commit some changes first

# Example 2: Last 2 commits
git format-patch -2
# 0001-first-commit.patch
# 0002-second-commit.patch

# Example 3: Output to directory
git format-patch -o patches/ -3
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
