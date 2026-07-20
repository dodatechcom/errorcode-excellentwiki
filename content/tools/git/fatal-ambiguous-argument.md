---
title: "[Solution] Git fatal: Ambiguous argument"
description: "Fix 'ambiguous argument' error. Resolve Git command failures when a reference name matches both a branch and a file or tag."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Ambiguous argument

fatal: ambiguous argument '<ref>': unknown revision or path not in the working tree.

This error occurs when Git cannot determine whether a given argument refers to a revision (branch/tag/commit) or a file path. The argument matches both.

## Common Causes

- A branch and a file share the same name
- A tag name conflicts with a branch name
- A commit SHA is incomplete or ambiguous
- Special characters in argument not quoted

## How to Fix

### Disambiguate with `--`

```bash
git show <name> --   # treat as revision
git show -- <name>   # treat as path
```

### Use Full Reference Names

```bash
git show refs/heads/<branch>
git show refs/tags/<tag>
```

### Quote Arguments with Special Characters

```bash
git log "HEAD~1"
```

## Examples

```bash
# Example 1: Branch and file named 'test'
git log test
# fatal: ambiguous argument 'test': unknown revision or path not in the working tree.
# Fix: git log test --     (revision)  or  git log -- test     (path)

# Example 2: Tag and branch conflict
git show v1
# fatal: ambiguous argument 'v1'
# Fix: git show refs/tags/v1  or  git show refs/heads/v1

# Example 3: Incomplete SHA
git show abc123
# fatal: ambiguous argument 'abc123'
# Fix: git show abc1234 (use at least 4-7 hex digits that are unique)
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
