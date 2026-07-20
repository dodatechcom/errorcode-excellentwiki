---
title: "[Solution] Git describe error"
description: "Fix 'git describe' error. Resolve issues when describing a commit using the most recent tag reachable from it."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git describe error

fatal: No tags can describe '<commit>'.

This error occurs when `git describe` cannot find any tag reachable from the specified commit.

## Common Causes

- No tags exist in the repository
- Current commit is ahead of all tags
- Tags are not reachable from the current commit
- Repository has no tags at all
- Commit is on a different branch without tags

## How to Fix

### Create a Tag

```bash
git tag -a v1.0.0 -m "Initial version"
git describe
```

### Use Tags Flag

```bash
git describe --tags
```

### Use Always Flag

```bash
git describe --always
```

### List All Tags

```bash
git tag -l
```

## Examples

```bash
# Example 1: No tags
git describe HEAD
# fatal: No tags can describe 'abc1234'.
# Fix: git tag -a v1.0.0 -m "Initial release"

# Example 2: Use lightweight tags
git describe --tags
# v1.0.0-5-gabc1234

# Example 3: Fallback to hash
git describe --always
# abc1234
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
