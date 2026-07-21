---
title: "[Solution] Linux: ssh-kex-error -- SSH key exchange failure"
description: "Fix Linux SSH key exchange errors. KEX algorithm negotiation failure between SSH hosts."
os: ["linux"]
error-types: ["ssh-error"]
severities: ["error"]
---

# Linux: SSH Key Exchange Error

SSH key exchange errors occur when client and server cannot agree on KEX algorithm.

## Common Causes

- Both sides support different DH groups
- Old server lacking curve25519-sha256 support
- Client security policy excluding server algorithms
- diffie-hellman-group1-sha1 disabled on server
- Missing host key types for negotiation

## How to Fix

### 1. Check Supported Kex

```bash
ssh -Q kex
sshd -T | grep kexalgorithms
ssh -vv user@host 2>&1 | grep kex
```

### 2. Configure Common Algorithms

```bash
# /etc/ssh/sshd_config
KexAlgorithms curve25519-sha256,diffie-hellman-group16-sha512
```

### 3. Test Connection

```bash
sudo systemctl restart sshd
ssh -o KexAlgorithms=curve25519-sha256 user@host
```

## Examples

```bash
$ ssh -Q kex
curve25519-sha256
diffie-hellman-group16-sha512
diffie-hellman-group18-sha512
$ ssh -vv user@host 2>&1 | grep kex
no matching kex algorithm found
```
