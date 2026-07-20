---
title: "[Solution] Git fatal: Could not read from remote repository"
description: "Fix 'could not read from remote repository' error. Resolve Git remote connection failures and authentication issues."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Could not read from remote repository

fatal: Could not read from remote repository.

This error occurs when Git cannot connect to or read data from a remote repository. The issue is typically related to network connectivity, authentication, or repository access permissions.

## Common Causes

- Repository URL is incorrect
- No network connection or proxy issues
- SSH key is missing or not configured
- Insufficient permissions to access the repository
- Repository has been moved or deleted

## How to Fix

### Verify Remote URL

```bash
git remote -v
```

### Test Connection

```bash
ssh -T git@github.com
```

### Update Remote URL

```bash
git remote set-url origin <correct-url>
```

### Use HTTPS Instead of SSH

```bash
git remote set-url origin https://github.com/user/repo.git
```

### Check Network Connectivity

```bash
ping github.com
curl -I https://github.com
```

## Examples

```bash
# Example 1: Wrong remote URL
git remote -v
# origin  https://github.com/wrong/repo.git
# Fix: git remote set-url origin https://github.com/correct/repo.git

# Example 2: SSH key not added to ssh-agent
ssh-add -l
# The agent has no identities.
# Fix: ssh-add ~/.ssh/id_rsa

# Example 3: Repository access denied
git pull origin main
# fatal: Could not read from remote repository.
# Fix: verify you have access or use https://user:token@github.com/user/repo.git
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
