---
title: "SSH Keygen Permission Error"
description: "ssh-keygen fails due to file permission issues"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# SSH Keygen Permission Error

ssh-keygen fails due to file permission issues

## Common Causes

- ~/.ssh directory does not exist or wrong permissions
- Home directory not owned by current user
- umask prevents creation of private files
- Existing key file is read-only

## How to Fix

1. Create .ssh directory: `mkdir -p ~/.ssh && chmod 700 ~/.ssh`
2. Check home directory ownership: `ls -la ~`
3. Set correct umask: `umask 077`
4. Remove existing key if overwriting: `rm ~/.ssh/id_rsa`

## Examples

```bash
# Create .ssh directory with correct permissions
mkdir -p ~/.ssh && chmod 700 ~/.ssh

# Generate key with correct permissions
umask 077 && ssh-keygen -t ed25519 -C "user@example.com"
```
