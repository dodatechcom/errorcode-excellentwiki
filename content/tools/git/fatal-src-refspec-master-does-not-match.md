---
title: "[Solution] Git fatal: src refspec master does not match any"
description: "Fix 'src refspec master does not match any' error. Resolve Git push failures when the source branch does not exist locally."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: src refspec master does not match any

error: src refspec master does not match any

This error occurs when you try to push a branch that does not exist in your local repository. Git cannot find the commit or branch you specified as the source.

## Common Causes

- The branch name is misspelled (master vs main)
- No commits have been made yet in the repository
- The branch was deleted locally but still exists remotely
- Wrong branch name specified in the push command

## How to Fix

### Check Existing Branches

```bash
git branch -a
```

### Create an Initial Commit

```bash
git add .
git commit -m "Initial commit"
```

### Use Correct Branch Name

```bash
# Check default branch name
git symbolic-ref HEAD
# Push with correct name
git push origin main
```

### Rename Branch

```bash
git branch -m master main
git push origin main
```

## Examples

```bash
# Example 1: No commits yet
git init
git push origin master
# error: src refspec master does not match any
# Fix: git add . && git commit -m "Initial commit" && git push origin master

# Example 2: Wrong branch name (main vs master)
git push origin master
# error: src refspec master does not match any
# Fix: git push origin main

# Example 3: Branch was deleted
git branch -D feature/x
git push origin feature/x
# error: src refspec feature/x does not match any
# Fix: recreate branch or delete remote reference
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
