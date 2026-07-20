---
title: "[Solution] Git fatal: bad object"
description: "Fix 'bad object' error. Resolve Git repository corruption issues where objects are damaged or missing."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: bad object

fatal: bad object HEAD

This error indicates that a Git object (commit, tree, or blob) in your repository is corrupted or unreadable. The repository integrity is compromised.

## Common Causes

- Hardware failure or disk write errors
- Repository interrupted during a write operation
- Improperly shut down Git operations
- File system corruption
- Manual editing of files in .git directory

## How to Fix

### Run Git Fsck to Diagnose

```bash
git fsck --full
```

### Restore from Reflog

```bash
git reflog
git reset --hard HEAD@{n}
```

### Clone a Fresh Copy

```bash
cd ..
rm -rf corrupted-repo
git clone <url>
```

### Recover from Remote

```bash
git fetch origin
git reset --hard origin/main
```

## Examples

```bash
# Example 1: Corrupted object
git fsck --full
# error: object xxx is a blob, not a commit
# Fix: clone a fresh copy

# Example 2: Bad HEAD
git status
# fatal: bad object HEAD
# Fix: git reflog && git reset --hard HEAD@{n}

# Example 3: After disk failure
cd /tmp
git clone https://github.com/user/repo.git
cp -a repo/.git /path/to/repo/
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
