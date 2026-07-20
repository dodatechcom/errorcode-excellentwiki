---
title: "[Solution] Git push tag to protected branch error"
description: "Fix Git push tag error when pushing to a branch with protected branch rules on GitHub or GitLab."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git push tag to protected branch error

! [remote rejected] v1.0 -> v1.0 (protected branch)

This error occurs when you try to push a tag to a branch that has protected branch rules configured on the remote server.

## Common Causes

- Branch is protected with push restrictions
- No permission to push tags to the branch
- Branch protection requires pull requests
- Repository admin has restricted direct pushes

## How to Fix

### Push Tags Separately

```bash
git push origin v1.0
```

### Push to Non-Protected Branch

```bash
git push origin feature/branch
```

### Create a Pull Request

```bash
# Push branch and create PR on GitHub
git push origin feature/new
gh pr create
```

### Request Repository Access

```bash
# Contact repository admin for access
```

## Examples

```bash
# Example 1: Tag rejected due to protection
git push origin main --tags
# ! [remote rejected] v1.0 -> v1.0 (protected branch)
# Fix: git push origin v1.0

# Example 2: Push to feature branch
git push origin feature/new-feature

# Example 3: Create PR from command line
git push origin feature/new-feature
gh pr create --title "New feature" --body "Description"
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
