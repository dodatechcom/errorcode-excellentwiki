---
title: "[Solution] Git fatal: Needed a single revision"
description: "Fix 'Needed a single revision' error. Resolve Git command failures when a commit reference resolves to multiple revisions."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Needed a single revision

fatal: Needed a single revision

This error occurs when a Git command that expects a single commit revision receives a reference that resolves to multiple commits.

## Common Causes

- Using a branch name when a tag name was expected
- Reference matches multiple objects
- Merged branch has multiple parents
- Ambiguous short SHA reference

## How to Fix

### Use a Specific Commit SHA

```bash
git show <full-commit-sha>
```

### Use Explicit Reference Path

```bash
git show refs/heads/<branch>
git show refs/tags/<tag>
```

### Check What the Reference Resolves To

```bash
git rev-parse <ref>
```

## Examples

```bash
# Example 1: Merge commit has multiple parents
git rev-parse HEAD
git show HEAD^
# fatal: Needed a single revision
# Fix: git show HEAD^1 (first parent) or HEAD^2 (second parent)

# Example 2: Ambiguous reference
git show main
# fatal: Needed a single revision
# Fix: git show refs/heads/main

# Example 3: Short SHA collision
git show abcdef1
# fatal: Needed a single revision
# Fix: provide complete SHA
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
