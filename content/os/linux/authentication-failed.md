---
title: "[Solution] Linux: authentication-failed — authentication failure"
description: "Fix Linux authentication-failed errors. authentication failure with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["security"]
weight: 6
---

# Linux: Authentication Failed

Authentication failures occur when login credentials cannot be verified.

## Common Causes

- Incorrect password or expired credentials
- SSH key not in authorized_keys
- PAM configuration blocking login
- Account locked or disabled
- AuthenticationMethods restriction in SSH config

## How to Fix

### 1. Check Authentication Logs

```bash
sudo journalctl -u sshd | grep "Failed\|denied" | tail -20
sudo tail -20 /var/log/auth.log
```

### 2. Verify Credentials

```bash
ssh -vvv user@localhost 2>&1 | grep "auth\|perm\|denied"
```

### 3. Check PAM Configuration

```bash
cat /etc/pam.d/sshd | grep -v "^#"
cat /etc/pam.d/common-auth | grep -v "^#"
```

### 4. Reset Password

```bash
sudo passwd <username>
```

## Examples

```bash
$ sudo journalctl -u sshd | grep "Failed password" | tail -3
Jul 20 14:30:45 server sshd[12345]: Failed password for john from 10.0.0.100 port 54321 ssh2

$ ssh -vvv user@localhost 2>&1 | grep "auth"
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: password
user@localhost's password:
# Authentication succeeded
```
