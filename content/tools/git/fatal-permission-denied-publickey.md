---
title: "[Solution] Git fatal: Permission denied (publickey)"
description: "Fix 'Permission denied (publickey)' error. Resolve Git SSH authentication failures when connecting to remote repositories."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Permission denied (publickey)

Permission denied (publickey).

This error occurs when Git's SSH connection attempt fails because no valid SSH key is provided or the key is not authorized on the remote server.

## Common Causes

- SSH key is not generated on your machine
- Public key is not added to GitHub/GitLab/Bitbucket
- Wrong SSH key is being used
- ssh-agent is not running or has no keys loaded
- Wrong remote URL format (using HTTPS instead of SSH)

## How to Fix

### Generate an SSH Key

```bash
ssh-keygen -t ed25519 -C "your@email.com"
```

### Add Key to ssh-agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### Copy Public Key to Clipboard

```bash
cat ~/.ssh/id_ed25519.pub
```

Add this key to your GitHub account under Settings > SSH and GPG keys.

### Test Connection

```bash
ssh -T git@github.com
```

## Examples

```bash
# Example 1: No SSH key
git clone git@github.com:user/repo.git
# Permission denied (publickey).
# Fix: ssh-keygen -t ed25519 -C "your@email.com" && cat ~/.ssh/id_ed25519.pub

# Example 2: Key not added to GitHub
ssh -T git@github.com
# Permission denied (publickey).
# Fix: add public key to GitHub account

# Example 3: Wrong key loaded
ssh-add -l
# 256 SHA256:xxx wrong-key@host (ED25519)
# Fix: ssh-add ~/.ssh/id_rsa && ssh -T git@github.com
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
