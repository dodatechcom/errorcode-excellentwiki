---
title: "[Solution] Git fatal: multiple updates for ref"
description: "Fix 'multiple updates for ref' error. Resolve Git push failures when the same reference is updated more than once in a single push."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: multiple updates for ref

fatal: multiple updates for ref '<ref>' not allowed.

This error occurs when you try to push multiple updates to the same reference (branch or tag) in a single push command. Git does not allow updating the same ref more than once.

## Common Causes

- Duplicate branch names in git push command
- Pushing both a branch and a tag with the same name
- Script or automation generating duplicate ref specs
- Using both full and short ref names
- `--mirror` push with conflicting refs

## How to Fix

### Remove Duplicate Refspecs

```bash
git push origin main
# Instead of: git push origin main main
```

### Push Separately

```bash
git push origin main
git push origin v1.0
```

### Use Specific Refspecs

```bash
git push origin refs/heads/main:refs/heads/main
```

### Avoid Mirror Pushes

```bash
git push origin main --no-mirror
```

## Examples

```bash
# Example 1: Duplicate in command
git push origin main main
# fatal: multiple updates for ref 'refs/heads/main' not allowed.
# Fix: git push origin main

# Example 2: Branch and tag with same name
git push origin main v1.0
# OK if they are different
# Duplicate if same: git push origin main v1.0

# Example 3: Script issue
# Fix: check push script for duplicate entries
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
