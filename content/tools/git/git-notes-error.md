---
title: "[Solution] Git notes error"
description: "Fix 'git notes' error. Resolve issues when adding, appending, or managing Git notes on commits."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git notes error

fatal: No note found for object <hash>

This error occurs when you try to show or manipulate a Git note on a commit that does not have any notes.

## Common Causes

- No notes have been added to the commit
- Notes ref is set incorrectly
- Notes were garbage collected
- Wrong commit hash specified

## How to Fix

### Add a Note

```bash
git notes add -m "Note content" <commit>
```

### List Notes

```bash
git notes list
```

### Show Notes for Commit

```bash
git notes show HEAD
```

### Configure Notes Display

```bash
git log --show-notes=*
```

## Examples

```bash
# Example 1: Add note
git notes add -m "This commit introduced a regression" abc1234

# Example 2: Append to existing note
git notes append -m "Also affects login flow" abc1234

# Example 3: Show all notes
git log --show-notes=*
# Displays notes alongside commits
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
