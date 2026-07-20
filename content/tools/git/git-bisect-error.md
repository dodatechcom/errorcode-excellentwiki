---
title: "[Solution] Git bisect error"
description: "Fix 'git bisect' error. Resolve issues when using Git bisect to find the commit that introduced a bug."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git bisect error

fatal: bisect run failed: exit code <n> from <command>

This error occurs when the bisect run script exits with a non-zero code that is not 0 (good), 1 (bad), or 125 (skip).

## Common Causes

- Bisect script itself has a bug
- Wrong boundaries (good/bad) set incorrectly
- Too many commits to bisect efficiently
- Script environment differs from expected
- Git state issues during bisect

## How to Fix

### Reset Bisect

```bash
git bisect reset
```

### Check Good/Bad Markers

```bash
git bisect log
```

### Restart with Correct Boundaries

```bash
git bisect start
git bisect good <known-good-commit>
git bisect bad <known-bad-commit>
```

### Run Bisect Manually

```bash
git bisect good  # or bad at each step
```

## Examples

```bash
# Example 1: Reset and restart
git bisect reset
git bisect start
git bisect good v1.0
git bisect bad HEAD
git bisect run npm test

# Example 2: Check bisect log
git bisect log

# Example 3: Manual bisect
git bisect start HEAD v1.0
# Test manually at each step
git bisect good  # or git bisect bad
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
