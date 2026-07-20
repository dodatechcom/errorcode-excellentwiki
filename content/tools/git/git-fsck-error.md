---
title: "[Solution] Git fsck (filesystem check) error"
description: "Fix 'git fsck' errors. Resolve repository corruption detected by Git's integrity checking tool."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fsck (filesystem check) error

error: object <hash>: is a blob, not a commit

This error occurs when `git fsck` finds inconsistencies or corruption in the Git object database.

## Common Causes

- Corrupted objects from hardware failure
- Manual manipulation of .git directory
- Incomplete Git operations
- Disk write errors during commits
- File system corruption

## How to Fix

### Run Full Fsck

```bash
git fsck --full
```

### Fix Missing Objects

```bash
git fetch origin
git fsck --full
```

### Restore from Remote

```bash
git fetch origin
git reset --hard origin/main
```

### Clone Fresh Copy

```bash
cd ..
rm -rf repo
git clone <url>
```

## Examples

```bash
# Example 1: Run diagnostics
git fsck --full
# Checking object directories: 100%
# dangling commit abc1234

# Example 2: Fix with fetch
git fetch origin --refetch
git fsck --full

# Example 3: Full recovery
cd /tmp
git clone <url> repo-fresh
mv repo/.git/objects/pack/* repo-fresh/.git/objects/pack/
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
