---
title: "[Solution] Git Push Rejected Error"
description: "Fix Git push rejected errors when commits are rejected by the remote server."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Push Rejected Error

Git push is rejected by the remote server.

```
! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs
```

## Common Causes

- Branch protection rules enabled
- Force push not allowed on protected branch
- Non-fast-forward push
- Commit message validation failing
- Server hooks rejecting push

## How to Fix

### Check Branch Protection

```bash
# Check protected branch rules
git push 2>&1 | grep -i "protected\|hook\|rejected"

# Try pushing to different branch
git push origin feature-branch:refs/heads/feature-branch
```

### Force Push (Use with Caution)

```bash
# Force push to rewrite remote history
git push --force

# Safer force push
git push --force-with-lease
```

### Create Pull Request Instead

```bash
# Push feature branch
git push -u origin feature-branch

# Create PR through GitHub/GitLab UI
```

### Fix Commit Message

```bash
# Amend last commit message
git commit --amend -m "New message"

# Force push amended commit
git push --force-with-lease
```

### Check Pre-receive Hooks

```bash
# Contact server admin to check hooks
# Common hook issues:
# - Sign-off required (add -s to commits)
# - DCO sign-off
# - Commit message format
git commit -s -m "Signed-off-by commit"
```

## Examples

```bash
# Safe push workflow
git fetch origin
git log --oneline HEAD..origin/main

# If behind, pull first
git pull --rebase origin main
git push origin main
```
