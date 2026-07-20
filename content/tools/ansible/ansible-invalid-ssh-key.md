---
title: "[Solution] Ansible Invalid SSH Key"
description: "Fix Ansible errors caused by invalid or corrupted SSH private keys"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot use the provided SSH key for authentication.

```
Permissions 0644 for /home/admin/.ssh/id_rsa are too open.
```

## Common Causes

- SSH key file permissions too open
- Corrupted private key file
- Wrong key format
- Key passphrase not provided

## How to Fix

```bash
# Fix key permissions
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub

# Verify key integrity
ssh-keygen -l -f ~/.ssh/id_rsa

# Generate a new key pair
ssh-keygen -t ed25519 -C \"ansible-deploy\" -f ~/.ssh/ansible_deploy -N \"\"
ssh-copy-id -i ~/.ssh/ansible_deploy.pub admin@192.168.1.100
```
