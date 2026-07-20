---
title: "[Solution] Git fatal: Not a valid object name"
description: "Fix 'Not a valid object name' error. Resolve Git command failures when a commit, tree, or blob reference is invalid."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Not a valid object name

fatal: Not a valid object name '<ref>'.

This error occurs when you reference a Git object (commit, tree, tag, blob) that does not exist or has an invalid format.

## Common Causes

- Typo in commit SHA or reference name
- Reference to a commit from a different repository
- Object was garbage collected
- Corrupted repository objects
- Missing `-` in reference names

## How to Fix

### Verify Object Exists

```bash
git cat-file -t <ref>
```

### List Recent Commits

```bash
git log --oneline -5
```

### Check Reflog for Lost Commits

```bash
git reflog
```

### Verify Tag Names

```bash
git tag -l
```

## Examples

```bash
# Example 1: Typo in commit hash
git show 1a2b3c4
# fatal: Not a valid object name '1a2b3c4'
# Fix: use correct hash git show 1a2b3c4d5e

# Example 2: Reference to deleted commit
git show HEAD@{5}
# fatal: Not a valid object name
# Fix: check reflog for valid references

# Example 3: Wrong tag
git show v1.0.0
# fatal: Not a valid object name 'v1.0.0'
# Fix: git tag -l to list valid tags
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
