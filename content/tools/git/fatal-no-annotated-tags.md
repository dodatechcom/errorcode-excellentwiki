---
title: "[Solution] Git fatal: No annotated tags"
description: "Fix 'No annotated tags' error. Resolve Git describe failures when no annotated tags exist in the repository."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: No annotated tags

fatal: No annotated tags can describe '<commit>'.

This error occurs when `git describe` cannot find an annotated tag that can be used to describe the current commit.

## Common Causes

- No annotated tags in the repository
- Tags exist but are lightweight (not annotated)
- Current commit is ahead of all existing tags
- Tags were created without the `-a` flag

## How to Fix

### Create an Annotated Tag

```bash
git tag -a v1.0.0 -m "Version 1.0.0"
```

### Use Lightweight Tags with Describe

```bash
git describe --tags
```

### Use --always Flag

```bash
git describe --always
```

### List Existing Tags

```bash
git tag -l
```

## Examples

```bash
# Example 1: No annotated tags
git describe
# fatal: No annotated tags can describe 'abc1234'.
# Fix: git tag -a v1.0.0 -m "Initial release" && git describe

# Example 2: Use --tags flag
git describe --tags
# v1.0.0-5-gabc1234

# Example 3: Use commit hash fallback
git describe --always
# abc1234
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
