---
title: "[Solution] Git mergetool error"
description: "Fix 'git mergetool' error. Resolve issues when launching merge conflict resolution tools."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git mergetool error

No files need merging

This error occurs when you run `git mergetool` but there are no merge conflicts to resolve in the working tree.

## Common Causes

- No merge or rebase in progress
- All conflicts were already resolved
- Running in a directory without conflicts
- Merge completed successfully without conflicts
- Wrong repository

## How to Fix

### Check for Merge in Progress

```bash
git status
```

### Verify Conflict Files

```bash
git diff --name-only --diff-filter=U
```

### Configure Mergetool

```bash
git config merge.tool vimdiff
git config mergetool.keepBackup false
```

### List Available Tools

```bash
git mergetool --tool-help
```

## Examples

```bash
# Example 1: No conflicts
git mergetool
# No files need merging
# Fix: check git status first

# Example 2: Configure and run
git config merge.tool vimdiff
git config mergetool.keepBackup false
git merge feature/branch
git mergetool
# Opens vimdiff for each conflicted file

# Example 3: Use VS Code as mergetool
git config merge.tool vscode
git config mergetool.vscode.cmd 'code --wait $MERGED'
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
