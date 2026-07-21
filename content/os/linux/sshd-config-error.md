---
title: "[Solution] Linux: sshd-config-error -- sshd config syntax error"
description: "Fix Linux sshd config errors. SSH daemon configuration syntax error preventing start."
os: ["linux"]
error-types: ["ssh-error"]
severities: ["error"]
---

# Linux: SSHD Config Error

SSHD configuration errors prevent the SSH daemon from starting.

## Common Causes

- Deprecated directive in new OpenSSH version
- Invalid keyword or value in sshd_config
- Incorrect path in HostKey or AuthorizedKeysFile
- Multiple ListenAddress conflicts
- Ciphers or MACs containing unsupported algorithms

## How to Fix

### 1. Test Configuration

```bash
sudo sshd -t
sudo sshd -T | head -20
```

### 2. Find Syntax Error

```bash
sudo sshd -T 2>&1 | grep -i error
sudo sshd -d -p 2222 2>&1 | head -20
```

### 3. Fix Configuration

```bash
sudo vim /etc/ssh/sshd_config
# Comment out deprecated directives
sudo systemctl restart sshd
```

## Examples

```bash
$ sudo sshd -t
/etc/ssh/sshd_config line 42: Deprecated option UsePrivilegeSeparation
$ sudo vim /etc/ssh/sshd_config
# Remove deprecated lines
$ sudo sshd -t
# No output = valid config
```
