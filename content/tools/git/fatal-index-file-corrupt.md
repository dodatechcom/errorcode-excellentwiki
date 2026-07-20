---
title: "[Solution] Git fatal: index file corrupt"
description: "Fix 'index file corrupt' error. Resolve Git index corruption issues that prevent repository operations."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: index file corrupt

fatal: index file corrupt

This error occurs when Git's index file (`.git/index`) is corrupted. The index tracks staged changes and working tree state.

## Common Causes

- Improper shutdown during a Git operation
- Disk write error while updating the index
- Manual editing or deletion of `.git/index`
- File system corruption
- Running out of disk space during index update

## How to Fix

### Remove and Rebuild Index

```bash
rm -f .git/index
git reset HEAD
```

### Restore Index from Backup

```bash
# Git stores index backup
git fsck
```

### Reset to Last Commit

```bash
git reset HEAD -- .
```

### Check for Other Corrupt Files

```bash
git fsck --full
```

## Examples

```bash
# Example 1: Corrupted index
git status
# fatal: index file corrupt
# Fix: rm -f .git/index && git reset HEAD

# Example 2: Rebuild from scratch
rm -f .git/index
git add -A
git commit -m "Rebuild index"

# Example 3: After disk full recovery
df -h .
# Free up space
rm -f .git/index
git reset HEAD
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
