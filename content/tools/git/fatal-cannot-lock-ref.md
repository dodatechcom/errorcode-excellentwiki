---
title: "[Solution] Git fatal: cannot lock ref"
description: "Fix 'cannot lock ref' error. Resolve Git reference update failures when the lock file for a reference already exists."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: cannot lock ref

fatal: cannot lock ref '<ref>': is at <hash> but expected <hash>

This error occurs when Git cannot lock a reference (branch or tag) because another process is holding the lock, or the reference state does not match expectations.

## Common Causes

- Another Git process is running in the same repository
- Previous Git operation was interrupted
- Reference state mismatch between local and expected
- Race condition in concurrent Git operations
- Stale lock files in .git directory

## How to Fix

### Remove Stale Lock Files

```bash
rm -f .git/refs/heads/<branch>.lock
rm -f .git/refs/tags/<tag>.lock
rm -f .git/HEAD.lock
rm -f .git/index.lock
```

### Check for Running Git Processes

```bash
ps aux | grep git
kill <pid>
```

### Fetch and Reset

```bash
git fetch origin
git reset --hard origin/<branch>
```

## Examples

```bash
# Example 1: Stale lock file
rm -f .git/refs/heads/main.lock
git push origin main

# Example 2: Remove all lock files
find .git -name "*.lock" -delete
git status

# Example 3: Index lock
rm -f .git/index.lock
git add .
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
