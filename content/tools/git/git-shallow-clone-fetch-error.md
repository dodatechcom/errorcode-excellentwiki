---
title: "[Solution] Git shallow clone fetch error"
description: "Fix Git shallow clone fetch errors. Resolve issues when deepening or unshallowing a shallow clone."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git shallow clone fetch error

fatal: --depth is ignored in --unshallow

This error occurs when conflicting options are used while trying to deepen or unshallow a shallow clone.

## Common Causes

- Using `--depth` with `--unshallow` simultaneously
- Trying to deepen an already full repository
- Network issues during fetch on a shallow repo
- Server does not support shallow operations

## How to Fix

### Unshallow Completely

```bash
git fetch --unshallow
```

### Deepen by Specific Number

```bash
git fetch --depth=100
```

### Convert to Full Clone

```bash
git fetch --unshallow origin
git pull --all
```

### Check if Repository is Shallow

```bash
cat .git/shallow
```

## Examples

```bash
# Example 1: Unshallow clone
git fetch --unshallow origin
git pull --all

# Example 2: Deepen by 50 commits
git fetch --depth=50

# Example 3: Check shallow status
cat .git/shallow
# If file exists, repo is shallow
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
