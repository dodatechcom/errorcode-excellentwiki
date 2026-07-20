---
title: "[Solution] Git fetch prune error"
description: "Fix 'git fetch --prune' error. Resolve issues when pruning stale remote-tracking references during fetch."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fetch prune error

fatal: --prune requires a remote

This error occurs when you run `git fetch --prune` without specifying a remote. Git needs to know which remote's tracking branches to prune.

## Common Causes

- Remote name not provided
- No remotes configured in the repository
- Using `--prune` with an invalid remote name
- Typo in the remote name

## How to Fix

### Specify the Remote

```bash
git fetch --prune origin
```

### Prune All Remotes

```bash
git remote prune origin
```

### Configure Automatic Pruning

```bash
git config --global fetch.prune true
```

### Check Configured Remotes

```bash
git remote -v
```

## Examples

```bash
# Example 1: Missing remote
git fetch --prune
# fatal: --prune requires a remote
# Fix: git fetch --prune origin

# Example 2: Configure automatic prune
git config --global fetch.prune true
git fetch origin  # automatically prunes

# Example 3: Prune all stale branches
git remote prune origin --dry-run  # preview
git remote prune origin  # execute
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
