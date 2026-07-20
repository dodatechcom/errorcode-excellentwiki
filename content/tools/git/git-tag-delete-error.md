---
title: "[Solution] Git tag delete error"
description: "Fix 'git tag -d' error. Resolve failures when trying to delete Git tags."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git tag delete error

error: tag '<tag>' not found.

This error occurs when you try to delete a Git tag that does not exist locally.

## Common Causes

- Tag name is misspelled
- Tag exists remotely but not locally
- Tag was already deleted
- Wrong tag name format

## How to Fix

### List Local Tags

```bash
git tag -l
```

### Delete Local Tag

```bash
git tag -d <tag-name>
```

### Delete Remote Tag

```bash
git push origin --delete <tag-name>
```

### Fetch Tags First

```bash
git fetch --tags
git tag -d <tag-name>
```

## Examples

```bash
# Example 1: Tag not found
git tag -d v1.0
# error: tag 'v1.0' not found.
# Fix: git tag -l to see available tags
# Or: git tag -d v1.0.0 (correct name)

# Example 2: Delete local and remote
git tag -d v1.0
git push origin --delete v1.0

# Example 3: Delete remote only
git push origin :refs/tags/v1.0
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
