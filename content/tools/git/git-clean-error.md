---
title: "[Solution] Git clean error"
description: "Fix 'git clean' error. Resolve issues when removing untracked files and directories from the working tree."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git clean error

fatal: clean.requireForce and -n or -f not set

This error occurs when you run `git clean` without the force flag and the `clean.requireForce` config is set to true (default).

## Common Causes

- Running `git clean` without `-f` or `-n` flag
- `clean.requireForce` is enabled (default)
- Not previewing files before removing them
- Using `git clean` in a directory with important untracked files

## How to Fix

### Preview Files to Remove

```bash
git clean -n
```

### Force Remove Untracked Files

```bash
git clean -f
```

### Remove Untracked Directories

```bash
git clean -fd
```

### Remove Ignored Files Too

```bash
git clean -xfd
```

### Disable Force Requirement

```bash
git config --global clean.requireForce false
```

## Examples

```bash
# Example 1: Force required
git clean
# fatal: clean.requireForce and -n or -f not set
# Fix: git clean -f

# Example 2: Preview first
git clean -n
# Would remove build/

# Example 3: Remove everything
git clean -xfd
# Removes all untracked and ignored files
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
