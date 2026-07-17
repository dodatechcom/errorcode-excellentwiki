---
title: "[Solution] Git Merge Conflict — CONFLICT: Merge conflict in X"
description: "Fix Git merge conflict errors. Resolve CONFLICT: Merge conflict in X by editing conflicted files and completing the merge."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git Merge Conflict — CONFLICT: Merge conflict in X

A merge conflict occurs when Git cannot automatically reconcile changes from two branches. Both branches modified the same lines in a file, and Git needs you to manually decide which changes to keep.

## Common Causes

- Two branches modified the same lines in a file
- One branch deleted a file that the other branch modified
- Renaming a file in one branch while modifying it in another
- Merging branches that have diverged significantly over time

## How to Fix

### Identify Conflicted Files

```bash
git status
```

Look for files listed under "Unmerged paths".

### Edit Conflicted Files

Open the conflicted file and look for conflict markers:

```
<<<<<<< HEAD
your changes here
=======
incoming changes here
>>>>>>> branch-name
```

Choose which changes to keep, remove the markers, and save the file.

### Mark Conflicts as Resolved

```bash
git add <resolved-file>
```

### Complete the Merge

```bash
git commit
```

### Abort the Merge (if needed)

```bash
git merge --abort
```

## Examples

```bash
# Example 1: Merge feature branch into main
git checkout main
git merge feature/login
# CONFLICT (content): Merge conflict in src/auth.js

# Example 2: Resolve and continue
# Edit src/auth.js, remove conflict markers
git add src/auth.js
git commit -m "Merge feature/login, resolve auth.js conflict"

# Example 3: Use a merge tool
git mergetool
```

## Related Errors

- [Detached HEAD]({{< relref "/tools/git/detached-head" >}}) — working on a commit not attached to a branch
- [Image Not Found]({{< relref "/tools/docker/image-not-found" >}}) — Docker image errors when deploying after merge
