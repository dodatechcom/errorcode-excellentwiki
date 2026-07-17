---
title: "[Solution] Git Stash Apply Error — stash apply failed"
description: "Fix Git stash apply errors. Resolve conflicts when applying stashed changes."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A stash apply error occurs when Git cannot cleanly apply stashed changes to the current working tree. This happens when the stashed changes conflict with the current state of the files.

## Common Causes

- The same files have been modified since the stash was created
- The stash was created on a different branch with different file states
- Files were deleted from the working tree since the stash was created
- The stash contains changes that overlap with uncommitted changes

## How to Fix

### Check Stash Contents

```bash
git stash show
git stash show -p stash@{0}
```

### Apply Stash and Resolve Conflicts

```bash
git stash apply
# resolve conflicts
git add <resolved-file>
```

### Drop Stash After Applying

```bash
git stash drop stash@{0}
```

### View All Stashes

```bash
git stash list
```

### Apply a Specific Stash

```bash
git stash apply stash@{2}
```

## Examples

```bash
# Example 1: Apply stash with conflicts
git stash apply
# CONFLICT (content): Merge conflict in src/config.js

# Resolve conflicts
git add src/config.js
git commit -m "Resolve stash conflict in config.js"

# Example 2: Apply stash from different branch
git stash list
# stash@{0}: On feature: WIP: refactor auth
git stash apply stash@{0}
```

## Related Errors

- [Git Merge Conflict]({{< relref "/tools/git/git-merge-conflict" >}}) — merge conflict resolution
- [Git Detached HEAD]({{< relref "/tools/git/git-detached-head" >}}) — HEAD detached at commit
