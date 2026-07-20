---
title: "[Solution] Git fatal: Could not find remote ref"
description: "Fix 'could not find remote ref' error. Resolve Git fetch and pull failures when a remote branch reference does not exist."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Could not find remote ref

fatal: Could not find remote ref <ref>.

This error occurs when you try to fetch or pull a remote reference (branch or tag) that does not exist on the remote server.

## Common Causes

- The branch was deleted on the remote
- Typo in the branch or tag name
- The branch exists under a different name
- Remote has not been fetched recently
- Tag name is incorrect

## How to Fix

### List Remote Branches

```bash
git ls-remote --heads origin
```

### List Remote Tags

```bash
git ls-remote --tags origin
```

### Fetch All Remote References

```bash
git fetch origin
```

### Verify Branch Name

```bash
git branch -r
```

## Examples

```bash
# Example 1: Deleted remote branch
git fetch origin feature/deleted-branch
# fatal: Could not find remote ref feature/deleted-branch
# Fix: check active branches with git branch -r

# Example 2: Typo in branch name
git pull origin featuer/login
# fatal: Could not find remote ref featuer/login
# Fix: git pull origin feature/login

# Example 3: Tag name mismatch
git fetch origin v1.0
# fatal: Could not find remote ref v1.0
# Fix: git ls-remote --tags origin to list available tags
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
