---
title: "[Solution] Git fatal: cannot update ref"
description: "Fix 'cannot update ref' error. Resolve Git failures when updating branch or tag references due to conflicts or locks."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: cannot update ref

fatal: cannot update ref '<ref>': trying to write non-commit <hash>

This error occurs when Git tries to update a reference to point to a non-commit object. References like branches should always point to commits.

## Common Causes

- Trying to push a tag that points to a non-commit
- Corrupted reference file
- Manual modification of reference files
- Attempting to point a branch to a tree or blob
- Fast-forward check failure

## How to Fix

### Check Reference Target

```bash
git cat-file -t <ref>
```

### Force Update Reference

```bash
git update-ref -f <ref> <hash>
```

### Delete and Recreate Reference

```bash
git branch -d <branch>
git checkout -b <branch> <hash>
```

### Check Repository Integrity

```bash
git fsck --full
```

## Examples

```bash
# Example 1: Tag pointing to wrong object
git update-ref refs/tags/v1.0 <commit-hash>

# Example 2: Force update branch
git update-ref -f refs/heads/main <commit-hash>

# Example 3: Delete and recreate
git branch -D feature/x
git checkout -b feature/x <correct-commit>
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
