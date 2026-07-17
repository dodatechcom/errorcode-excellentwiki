---
title: "[Solution] Git Merge Conflict in Specific File"
description: "Fix Git merge conflict in a specific file. Resolve CONFLICT messages for individual files during merge."
tools: ["git"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["merge-conflict", "conflict", "merge", "file", "git"]
weight: 5
---

## What This Error Means

This error occurs when Git cannot automatically merge changes from two branches because both modified the same lines in a specific file. Git marks the file as "unmerged" and requires manual resolution before the merge can complete.

## Common Causes

- Two branches modified the same lines in the same file
- One branch edited a file while the other deleted it
- File was renamed in one branch and modified in another
- Conflicting changes to configuration or generated files
- Long-lived feature branches that diverged significantly

## How to Fix

### List Conflicted Files

```bash
git status
# Unmerged paths:
#   both modified:   src/config.js
```

### Resolve the Conflict in the File

Open the conflicted file and look for conflict markers:

```
<<<<<<< HEAD
your current branch changes
=======
incoming branch changes
>>>>>>> feature-branch
```

Remove the markers and keep the correct code, then save.

### Stage the Resolved File

```bash
git add src/config.js
```

### Continue the Merge

```bash
git commit
```

### Use a Merge Tool

```bash
git mergetool
```

### Abort the Merge if Needed

```bash
git merge --abort
```

## Examples

```bash
# Example 1: Merge feature branch, resolve one file
git merge feature/login
# CONFLICT (content): Merge conflict in src/auth.js

# Edit src/auth.js, remove markers
git add src/auth.js
git commit -m "Merge feature/login, resolve auth.js conflict"

# Example 2: See which files conflict
git diff --name-only --diff-filter=U

# Example 3: Accept theirs or ours for a specific file
git checkout --theirs src/config.js
git add src/config.js
git commit

# Example 4: Accept ours
git checkout --ours src/config.js
git add src/config.js
git commit
```

## Related Errors

- [Git Detached HEAD]({{< relref "/tools/git/git-detached-head-v2" >}}) — HEAD not on a branch
- [Git Rebase Abort]({{< relref "/tools/git/git-rebase-abort-v2" >}}) — rebase conflict handling
- [Git Cherry-pick Fail]({{< relref "/tools/git/git-cherry-pick-fail-v2" >}}) — cherry-pick conflict
