---
title: "[Solution] Git fatal: Unable to find"
description: "Fix 'Unable to find' error. Resolve Git failures when a required file, commit, or object cannot be located in the repository."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Unable to find

fatal: Unable to find '<path>'.

This error occurs when Git cannot locate a required file or reference in the repository. The specified item may be missing, deleted, or was never committed.

## Common Causes

- Referencing a file that was deleted
- Commit hash does not exist in repository
- Branch reference points to a non-existent commit
- File exists in working tree but not in index
- Repository is in a detached HEAD state without the expected history

## How to Fix

### Search Repository History

```bash
git log --all --full-history -- <file>
```

### Check if File is Tracked

```bash
git ls-files <file>
```

### Find Commit by Message

```bash
git log --all --oneline --grep="<keyword>"
```

### Restore Deleted File

```bash
git checkout <commit-hash>^ -- <file>
```

## Examples

```bash
# Example 1: File not tracked
git show HEAD:src/config.js
# fatal: Unable to find 'src/config.js'
# Fix: add and commit the file first

# Example 2: Deleted file
git log --all --full-history -- src/config.js
# Shows commits where file existed
# Fix: git checkout <hash>^ -- src/config.js

# Example 3: Non-existent commit
git checkout 1a2b3c4
# fatal: Unable to find '1a2b3c4'
# Fix: use git log to find valid commit hashes
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
