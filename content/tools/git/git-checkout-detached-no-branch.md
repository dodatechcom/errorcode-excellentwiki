---
title: "[Solution] Git checkout detached HEAD no branch"
description: "Fix Git detached HEAD state. Resolve issues when Git HEAD is not attached to any branch, making commits potentially unreachable."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git checkout detached HEAD no branch

You are in 'detached HEAD' state.

This message occurs when you check out a specific commit, tag, or remote branch, making HEAD point directly to a commit instead of a branch.

## Common Causes

- Checking out a specific commit hash
- Checking out a tag
- Checking out a remote branch without creating a local branch
- Using `git checkout origin/<branch>` instead of just `<branch>`

## How to Fix

### Create a Branch from Detached HEAD

```bash
git switch -c <new-branch>
```

### Check Out Existing Branch

```bash
git checkout <existing-branch>
```

### Keep Changes Made in Detached State

```bash
git checkout -b <new-branch>
git add -A && git commit -m "Changes from detached HEAD"
```

### Discard Changes and Return to Branch

```bash
git checkout main
```

## Examples

```bash
# Example 1: Create branch to save changes
git checkout -b saved-changes
git add -A
git commit -m "Work done in detached HEAD"

# Example 2: Return to main
git checkout main

# Example 3: Checkout tag and make changes
git checkout v1.0
git checkout -b v1.0-patches
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
