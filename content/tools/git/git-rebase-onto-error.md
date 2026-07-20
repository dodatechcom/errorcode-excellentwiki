---
title: "[Solution] Git rebase --onto error"
description: "Fix 'git rebase --onto' error. Resolve issues when using rebase with the --onto option to transplant commits."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git rebase --onto error

fatal: invalid upstream '<ref>'

This error occurs when you provide an invalid reference to `git rebase --onto`. The upstream or new base reference cannot be found.

## Common Causes

- Typo in branch or reference name
- Reference does not exist
- References from a different repository
- `--onto` arguments in wrong order

## How to Fix

### Check Syntax

```bash
git rebase --onto <new-base> <upstream> <branch>
```

### Verify References Exist

```bash
git branch -a | grep <branch>
git log --oneline -5 <ref>
```

### Use Commits Instead of Branches

```bash
git rebase --onto <commit> <upstream-commit> <branch>
```

## Examples

```bash
# Example 1: Move last 3 commits from feature to main
git rebase --onto main feature~3 feature

# Example 2: Wrong reference
git rebase --onto main nonexistent feature
# fatal: invalid upstream 'nonexistent'
# Fix: git branch -a to find correct name

# Example 3: Correct order
git rebase --onto main feature-branch~3 feature-branch
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
