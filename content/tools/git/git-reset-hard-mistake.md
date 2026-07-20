---
title: "[Solution] Git reset --hard mistake recovery"
description: "Recover from accidental 'git reset --hard' mistake. Restore lost commits and changes after a hard reset."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git reset --hard mistake recovery

Recovering from accidental git reset --hard

Running `git reset --hard` discards all uncommitted changes and moves HEAD to a specified commit. If you reset to the wrong commit, your work is not necessarily lost.

## Recovery Methods

### Use Reflog to Find Lost Commits

```bash
git reflog
git reset --hard HEAD@{n}
```

### Recover Staged Changes

```bash
git fsck --lost-found
git show <lost-commit>
```

### Find Dangling Commits

```bash
git fsck --full --no-dangling
```

## Examples

```bash
# Example 1: Undo reset --hard
git reflog
# abc1234 HEAD@{0}: reset: moving to HEAD~2
# def5678 HEAD@{1}: commit: Important changes
git reset --hard HEAD@{1}

# Example 2: Recover from fsck
git fsck --lost-found
# dangling commit abc1234
git show abc1234
git merge abc1234

# Example 3: ORIG_HEAD recovery
git reset --hard ORIG_HEAD
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
