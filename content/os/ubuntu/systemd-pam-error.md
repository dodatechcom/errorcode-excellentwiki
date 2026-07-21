---
title: "[Solution] Ubuntu Server: system-pam-error"
description: "Fix Ubuntu system-pam-error. PAM authentication module fails for systemd services."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd PAM Error

PAM authentication fails for systemd managed services.

## Common Causes
- /etc/pam.d/ configuration file corrupted
- pam_unix.so module missing
- pam_limits.so not applied
- PAM stack configuration error

## How to Fix
1. Check PAM configuration
```bash
ls /etc/pam.d/
cat /etc/pam.d/common-auth
```
2. Verify PAM modules exist
```bash
ls /lib/security/pam_*.so
ls /lib/x86_64-linux-gnu/security/pam_*.so
```
3. Check PAM errors in logs
```bash
journalctl | grep -i pam
tail -20 /var/log/auth.log
```

## Examples
```bash
$ tail -20 /var/log/auth.log
Mar 15 10:00 sshd[1234]: pam_unix(sshd:auth): conversation failed
Mar 15 10:00 sshd[1234]: pam_unix(sshd:auth): auth could not identify password
```
