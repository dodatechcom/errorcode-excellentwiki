---
title: "[Solution] Git Branch Operation Error"
description: "Fix Git branch creation, deletion, and checkout errors. Resolve branch name conflicts and operation failures."
tools: ["git"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["branch", "checkout", "create", "delete", "git"]
weight: 5
---

## What This Error Means

A Git branch error occurs when a branch operation (create, delete, rename, or checkout) fails. Common reasons include invalid branch names, the branch already existing, or trying to delete a branch that is currently checked out.

## Common Causes

- Branch name already exists or conflicts with an existing ref
- Invalid characters in the branch name
- Trying to delete the currently checked out branch
- Trying to delete a branch with unmerged commits
- Remote branch name conflicts with local branch

## How to Fix

### List Existing Branches

```bash
git branch -a
```

### Create a New Branch

```bash
git branch <branch-name>
git checkout -b <branch-name>
```

### Force Delete a Branch

```bash
git branch -D <branch-name>
```

### Rename a Branch

```bash
git branch -m <old-name> <new-name>
```

### Delete a Remote Branch

```bash
git push origin --delete <branch-name>
```

### Checkout a Branch

```bash
git checkout <branch-name>
# or
git switch <branch-name>
```

## Examples

```bash
# Example 1: Branch already exists
git branch feature/login
# fatal: A branch named 'feature/login' already exists.

# Fix: use a different name
git branch feature/login-v2

# Example 2: Can't delete checked-out branch
git branch -d main
# error: Cannot delete branch 'main' checked out at '/path/to/repo'

# Fix: switch to another branch first
git checkout feature
git branch -d main

# Example 3: Invalid branch name
git branch feature/my branch
# fatal: 'feature/my branch' is not a valid branch name

# Fix: use dashes or underscores
git branch feature/my-branch
```

## Related Errors

- [Git Detached HEAD]({{< relref "/tools/git/git-detached-head-v2" >}}) — HEAD not on a branch
- [Git Ref Ambiguous]({{< relref "/tools/git/git-ref-ambiguous" >}}) — ref name conflicts
- [Git Tag Error]({{< relref "/tools/git/git-tag-error" >}}) — tag creation error
