---
title: "[Solution] Git am (apply mailbox) error"
description: "Fix 'git am' error. Resolve issues when applying patches from a mailbox file or format-patch output."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git am (apply mailbox) error

Patch failed at <number> <commit-message>

This error occurs when `git am` cannot apply a patch from a mailbox file. The patch may conflict with the current branch state.

## Common Methods

### Resolve Patch Failure

```bash
# Fix conflicts manually
git add <resolved-files>
git am --continue
```

### Skip Failed Patch

```bash
git am --skip
```

### Abort Patch Application

```bash
git am --abort
```

### Apply with Reject Files

```bash
git am --reject <patch-file>
```

## Examples

```bash
# Example 1: Resolve patch conflict
git am patches/0001-fix-bug.patch
# Patch failed at 0001 fix bug
# Fix: edit files, git add ., git am --continue

# Example 2: Skip problematic patch
git am --skip

# Example 3: Apply with 3-way merge
git am --3way patches/*.patch
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
