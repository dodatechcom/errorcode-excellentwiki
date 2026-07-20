---
title: "[Solution] Git gc (garbage collection) error"
description: "Fix 'git gc' error. Resolve issues when Git garbage collection fails to clean up or optimize the repository."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git gc (garbage collection) error

error: failed to run git gc

This error occurs when Git garbage collection encounters an issue while cleaning up repository objects or optimizing storage.

## Common Causes

- Another Git process is running
- Insufficient disk space
- Repository corruption
- Lock file from previous GC
- Too large repository with many objects

## How to Fix

### Check for Running Processes

```bash
ps aux | grep git
```

### Remove GC Lock File

```bash
rm -f .git/gc.pid
```

### Run GC with Verbose

```bash
git gc --verbose
```

### Run Aggressive GC

```bash
git gc --aggressive
```

### Check Disk Space

```bash
df -h .
```

## Examples

```bash
# Example 1: GC locked
rm -f .git/gc.pid
git gc --verbose

# Example 2: Aggressive optimization
git gc --aggressive --prune=now
# Optimizes all packs (slower but thorough)

# Example 3: Auto GC
git config gc.auto 500
# Automatically runs GC when object count exceeds 500
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
