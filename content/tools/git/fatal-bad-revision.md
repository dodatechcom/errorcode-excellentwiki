---
title: "[Solution] Git fatal: bad revision"
description: "Fix 'bad revision' error. Resolve Git command failures when a revision specifier is invalid or does not exist."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: bad revision

fatal: bad revision '<ref>'

This error occurs when you provide a revision parameter that Git cannot parse or resolve to a valid commit in the repository.

## Common Causes

- Typo in commit hash, branch name, or tag name
- Using a reference from a different repository
- The commit was garbage collected
- Merged branch no longer exists as a reference
- Invalid revision syntax like `HEAD^^^` with too many carets

## How to Fix

### Check Available Revisions

```bash
git log --oneline -10
```

### Verify Branch and Tag Names

```bash
git branch -a
git tag -l
```

### Use Reflog for Lost References

```bash
git reflog show HEAD
```

### Use Full Commit Hash

```bash
git log --oneline
git show <full-hash>
```

## Examples

```bash
# Example 1: Typo in revision
git log HEAD~~~  # too many carets
# fatal: bad revision 'HEAD~~~'
# Fix: git log HEAD~3

# Example 2: Deleted branch
git show feature/deleted
# fatal: bad revision 'feature/deleted'
# Fix: git reflog | grep feature

# Example 3: Wrong tag name
git diff v1.0 v2.0
# fatal: bad revision 'v2.0'
# Fix: git tag -l to see available tags
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
