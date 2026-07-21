---
title: "[Solution] Git Reference Resolution Error"
description: "Fix Git reference resolution errors when Git cannot find or resolve a commit, branch, or tag."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Reference Resolution Error

Git cannot resolve a reference to a commit, branch, or tag.

```
error: pathspec 'feature-x' did not match
fatal: bad revision 'HEAD~abc'
```

## Common Causes

- Reference does not exist
- Typo in branch or tag name
- Stale local references
- Ambiguous reference name
- Detached HEAD state

## How to Fix

### List All References

```bash
# List local branches
git branch -a

# List all tags
git tag -l

# Show HEAD reflog
git reflog show
```

### Resolve Ambiguous References

```bash
# Check what a reference resolves to
git rev-parse HEAD
git rev-parse main
git rev-parse v1.0

# Disambiguate branch from tag
git rev-parse refs/heads/main
git rev-parse refs/tags/main
```

### Fetch Missing References

```bash
# Fetch all branches and tags
git fetch --all --tags

# Fetch specific remote branch
git fetch origin feature-branch
```

### Use Full Reference Path

```bash
# Instead of short name
git log refs/heads/feature-branch
git log refs/tags/v1.0

# Remote branch
git log origin/main
```

## Examples

```bash
# Find and checkout branch
git fetch origin
git checkout feature-new-api

# Check if ref exists
if git rev-parse --verify "refs/tags/v2.0" >/dev/null 2>&1; then
    echo "Tag v2.0 exists"
fi
```
