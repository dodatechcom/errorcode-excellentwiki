---
title: "[Solution] Git fatal: origin does not appear to be a git repository"
description: "Fix 'origin does not appear to be a git repository' error. Resolve Git remote configuration issues when the remote is missing or invalid."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: origin does not appear to be a git repository

fatal: '<remote>' does not appear to be a git repository

This error occurs when you try to use a remote name that is not configured or a URL that does not point to a valid Git repository.

## Common Causes

- Remote name was never added or was removed
- Typo in the remote name
- Remote URL is incorrect or the repository was moved/deleted
- Wrong case sensitivity in remote name
- Repository was initialized without a remote

## How to Fix

### View Configured Remotes

```bash
git remote -v
```

### Add the Remote

```bash
git remote add origin <repository-url>
```

### Correct the Remote URL

```bash
git remote set-url origin <correct-url>
```

### Remove and Re-add

```bash
git remote remove origin
git remote add origin <url>
```

## Examples

```bash
# Example 1: No remote configured
git remote -v
# (empty)
# Fix: git remote add origin https://github.com/user/repo.git

# Example 2: Typo in remote name
git push orign main
# fatal: 'orign' does not appear to be a git repository
# Fix: git push origin main

# Example 3: Wrong URL
git remote set-url origin https://github.com/user/wrong-repo.git
git push origin main
# fatal: 'origin' does not appear to be a git repository
# Fix: git remote set-url origin https://github.com/user/correct-repo.git
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
