---
title: "[Solution] Git fatal: Could not resolve HEAD"
description: "Fix 'Could not resolve HEAD' error. Resolve Git failures when the HEAD reference is missing or points to a non-existent commit."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Could not resolve HEAD

fatal: Could not resolve HEAD to a commit

This error occurs when Git cannot determine the commit that HEAD points to. This typically happens in a repository with no commits.

## Common Causes

- Repository has no commits yet (fresh `git init`)
- HEAD reference was deleted or corrupted
- Repository was partially initialized
- ORIG_HEAD or other special refs are missing
- Bare repository without an initial commit

## How to Fix

### Create Initial Commit

```bash
git add .
git commit -m "Initial commit"
```

### Check HEAD Content

```bash
cat .git/HEAD
```

### Create an Orphan Branch

```bash
git checkout --orphan main
git add .
git commit -m "Initial commit"
```

### Reinitialize Repository

```bash
rm -rf .git
git init
git add .
git commit -m "Initial commit"
```

## Examples

```bash
# Example 1: Fresh repository
git log
# fatal: Could not resolve HEAD to a commit
# Fix: git add . && git commit -m "Initial commit"

# Example 2: Corrupted HEAD
cat .git/HEAD
# ref: refs/heads/nonexistent
# Fix: echo "ref: refs/heads/main" > .git/HEAD && git commit --allow-empty -m "Init"

# Example 3: Reinitialize
rm -rf .git
git init
git add -A
git commit -m "Initial commit"
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
