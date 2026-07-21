---
title: "SSH Weak Cipher Algorithm Error"
description: "SSH connection rejected due to weak cipher algorithms"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# SSH Weak Cipher Algorithm Error

SSH connection rejected due to weak cipher algorithms

## Common Causes

- Server only accepts weak ciphers (3DES, RC4)
- Client configured to use deprecated algorithms
- FIPS mode requiring only approved algorithms
- Mismatched cipher lists between client and server

## How to Fix

1. Check server ciphers: `sshd -T | grep ciphers`
2. Update sshd_config: `Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com`
3. Test connection: `ssh -vvv user@host` for cipher negotiation
4. Regenerate host keys if needed

## Examples

```bash
# Check enabled ciphers on server
sudo sshd -T | grep ciphers

# Test SSH connection with verbose output
ssh -vvv user@host 2>&1 | grep -i cipher
```
