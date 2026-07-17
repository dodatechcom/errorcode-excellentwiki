---
title: "[Solution] Git Push Rejected — Non-fast-forward"
description: "Fix Git push rejected non-fast-forward errors. Resolve remote repository rejection when pushing."
tools: ["git"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A non-fast-forward push rejection means the remote branch has commits that your local branch does not have. Git blocks the push to prevent overwriting history. You must pull the remote changes first and integrate them before pushing.

## Common Causes

- Someone else pushed to the same branch since your last pull
- You rebased or amended commits that were already pushed
- The remote branch was force-pushed by another collaborator
- You are on a different branch than expected

## How to Fix

### Pull Remote Changes First

```bash
git pull origin main
# Resolve any conflicts, then push
git push origin main
```

### Rebase Before Pushing

```bash
git pull --rebase origin main
git push origin main
```

### Force Push (Use with Caution)

```bash
git push --force-with-lease origin main
```

### Check Remote State

```bash
git fetch origin
git log --oneline origin/main..HEAD
git log --oneline HEAD..origin/main
```

## Examples

```bash
# Example 1: Push rejected
git push origin main
# ! [rejected]        main -> main (non-fast-forward)
# error: failed to push some refs

# Fix: pull and merge
git pull origin main
git push origin main

# Example 2: Force push with lease (safer)
git push --force-with-lease origin feature
# Fails if someone else pushed since your last fetch

# Example 3: Rebase instead of merge
git pull --rebase origin main
# Successfully rebased and updated refs/heads/main.
git push origin main
```

## Related Errors

- [Git Fetch Error]({{< relref "/tools/git/git-fetch-error" >}}) — fetch failed
- [Git Merge Conflict]({{< relref "/tools/git/git-merge-conflict-v2" >}}) — merge conflict in file
- [Git LFS Push]({{< relref "/tools/git/git-lfs-push-v2" >}}) — LFS upload failed
