---
title: "[Solution] Git fatal: Refusing to merge unrelated histories"
description: "Fix 'refusing to merge unrelated histories' error. Resolve Git merge failures when branches have no common commit ancestor."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Refusing to merge unrelated histories

fatal: refusing to merge unrelated histories

This error occurs when you attempt to merge two branches or repositories that do not share a common commit ancestor. Git refuses the merge to prevent creating a broken history.

## Common Causes

- Merging two independent repositories
- Adding a new repository as a remote with no common history
- Rebasing a branch onto an unrelated branch
- Force-pushed a rewritten history that diverged completely

## How to Fix

### Allow Unrelated Histories (Merge)

```bash
git merge --allow-unrelated-histories <branch>
```

### Allow Unrelated Histories (Pull)

```bash
git pull origin <branch> --allow-unrelated-histories
```

### Fetch and Check History First

```bash
git fetch origin
git log --oneline --graph HEAD..origin/main | head -5
```

## Examples

```bash
# Example 1: Merge unrelated repository
git remote add upstream https://github.com/user/repo.git
git fetch upstream
git merge upstream/main
# fatal: refusing to merge unrelated histories
# Fix: git merge --allow-unrelated-histories upstream/main

# Example 2: Pull into fresh init
git init
git remote add origin https://github.com/user/repo.git
git pull origin main
# fatal: refusing to merge unrelated histories
# Fix: git pull origin main --allow-unrelated-histories

# Example 3: After force push rewrite
git pull origin main
# fatal: refusing to merge unrelated histories
# Fix: git fetch origin && git reset --hard origin/main
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
