---
title: "[Solution] Git Permission Denied SSH — Permission denied (publickey)"
description: "Fix Git SSH permission denied error. Resolve authentication issues when connecting to remote repositories."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git Permission Denied SSH — Permission denied (publickey)

This error occurs when SSH authentication fails when connecting to a Git remote. The server rejects your SSH key or credentials.

## Common Causes

- SSH key not added to the SSH agent
- Public key not added to the Git hosting service (GitHub, GitLab)
- Wrong SSH key being used
- SSH key permissions are too open

## How to Fix

### Check SSH Agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

### Test SSH Connection

```bash
ssh -T git@github.com
```

### Verify SSH Key is Added

```bash
ssh-add -l
```

### Fix SSH Key Permissions

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
```

### Use HTTPS Instead of SSH

```bash
git remote set-url origin https://github.com/user/repo.git
```

### Generate New SSH Key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

## Examples

```bash
# Example 1: SSH key not in agent
git push origin main
# Permission denied (publickey).
# Fix: eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_rsa

# Example 2: Test SSH connection
ssh -T git@github.com
# Hi username! You've successfully authenticated

# Example 3: Switch to HTTPS
git remote set-url origin https://github.com/user/repo.git
git push origin main
```

## Related Errors

- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — remote has changes you don't have
- [Permission Denied]({{< relref "/tools/docker/permission-denied3" >}}) — Docker permission issues
