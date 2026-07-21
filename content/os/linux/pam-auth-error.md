---
title: "[Solution] Linux: pam-auth-error -- PAM authentication failure"
description: "Fix Linux PAM authentication errors. PAM authentication stack failure preventing login."
os: ["linux"]
error-types: ["pam-error"]
severities: ["error"]
---

# Linux: PAM Authentication Error

PAM authentication errors prevent users from logging in or elevating privileges.

## Common Causes

- PAM module shared library not found
- Authentication stack configuration syntax error
- pam_unix.so cannot read /etc/shadow
- Missing or broken pam.d configuration
- SELinux blocking PAM module access

## How to Fix

### 1. Check PAM Configuration

```bash
cat /etc/pam.d/common-auth
cat /etc/pam.d/sudo
ls /lib/security/ | grep pam_
```

### 2. Debug PAM

```bash
sudo pamtester login <user> authenticate
journalctl -u sshd -n 20 | grep pam
```

### 3. Fix PAM Stack

```bash
sudo vim /etc/pam.d/common-auth
# Ensure: auth required pam_unix.so
sudo chmod 644 /etc/shadow 2>/dev/null
```

## Examples

```bash
$ journalctl -u sshd -n 5
sshd[1234]: pam_unix(sshd:auth): authentication failure
sshd[1234]: pam_unix(sshd:auth): conversation failed
$ sudo ls -la /etc/shadow
-rw------- 1 root shadow 1234 Jul 20 14:00 /etc/shadow
```
