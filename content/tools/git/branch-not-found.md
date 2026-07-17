---
title: "[Solution] Git Branch Not Found — pathspec 'X' did not match any branches"
description: "Fix Git branch not found error. Resolve pathspec did not match any branches known to git."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git Branch Not Found — pathspec 'X' did not match any branches

This error occurs when Git cannot find a branch with the specified name. The branch may not exist locally or remotely, or the name may be misspelled.

## Common Causes

- Typo in the branch name
- Branch exists only on the remote and hasn't been fetched
- Branch was already deleted locally or remotely
- Trying to checkout a tag or commit hash as a branch

## How to Fix

### List Local Branches

```bash
git branch
```

### List Remote Branches

```bash
git branch -r
```

### Fetch All Remote Branches

```bash
git fetch --all
```

### Create and Checkout a New Branch

```bash
git checkout -b <branch-name>
```

### Checkout a Remote Branch Locally

```bash
git checkout --track origin/<branch-name>
```

## Examples

```bash
# Example 1: Typo in branch name
git checkout feature/loogin
# error: pathspec 'feature/loogin' did not match any branches known to 'git'
# Fix: git checkout feature/login

# Example 2: Branch not fetched
git checkout feature/new-api
# error: pathspec 'feature/new-api' did not match any branches
# Fix: git fetch --all && git checkout feature/new-api

# Example 3: Branch was deleted
git branch -d old-feature
git checkout old-feature
# error: pathspec 'old-feature' did not match any branches
```

## Related Errors

- [Detached HEAD]({{< relref "/tools/git/detached-head" >}}) — working on a commit not attached to a branch
- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — conflict when merging branches
