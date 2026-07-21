---
title: "[Solution] Ubuntu Server: system-tmpfiles-error"
description: "Fix Ubuntu system-tmpfiles-error. systemd-tmpfiles cleanup or creation fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Tmpfiles Error

systemd-tmpfiles encounters errors creating or cleaning temporary files.

## Common Causes
- Disk full preventing tmp file creation
- Permission issue on /tmp or /var/tmp
- tmpfiles.d rules conflict
- Filesystem mounted with noexec on /tmp

## How to Fix
1. Check tmpfiles rules
```bash
ls /etc/tmpfiles.d/
ls /usr/lib/tmpfiles.d/
```
2. Manually clean tmp
```bash
sudo systemd-tmpfiles --clean
sudo systemd-tmpfiles --remove
```
3. Check /tmp permissions
```bash
ls -la / | grep tmp
mount | grep /tmp
```

## Examples
```bash
$ sudo systemd-tmpfiles --clean
Failed to clean up: Read-only file system

$ mount | grep /tmp
tmpfs on /tmp type tmpfs (rw,nosuid,nodev,noexec)
```
