---
title: "[Solution] Linux: ssh-cipher-mismatch -- SSH cipher mismatch"
description: "Fix Linux SSH cipher mismatch errors. SSH cipher negotiation failure between hosts."
os: ["linux"]
error-types: ["ssh-error"]
severities: ["error"]
---

# Linux: SSH Cipher Mismatch

SSH cipher mismatch occurs when client and server cannot agree on encryption algorithm.

## Common Causes

- Server uses only deprecated ciphers
- Client hardened to reject weak ciphers
- OpenSSH version too old for modern ciphers
- Policy file restricting available ciphers
- FIPS mode limiting cipher options

## How to Fix

### 1. Check Available Ciphers

```bash
ssh -vv localhost 2>&1 | grep -i cipher
ssh -Q cipher
sshd -T | grep ciphers
```

### 2. Configure Matching Ciphers

```bash
# Server: /etc/ssh/sshd_config
Ciphers aes256-gcm@openssh.com,chacha20-poly1305@openssh.com
# Client: ~/.ssh/config
Host *
    Ciphers aes256-gcm@openssh.com
```

### 3. Restart SSH

```bash
sudo systemctl restart sshd
ssh -o Ciphers=aes256-gcm@openssh.com user@host
```

## Examples

```bash
$ ssh -vv user@host 2>&1 | grep cipher
debug1: kex: algorithm: (no match)
debug1: no matching cipher found
$ ssh -Q cipher
3des-cbc
aes128-cbc
aes256-gcm@openssh.com
```
