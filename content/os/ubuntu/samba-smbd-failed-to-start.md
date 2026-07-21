---
title: "[Solution] Ubuntu Server: samba-smbd-failed-to-start"
description: "Fix Ubuntu samba-smbd-failed-to-start. smbd service fails to start on boot."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Samba Smbd Failed To Start

smbd service fails to start during system boot.

## Common Causes
- smb.conf syntax error
- Port 445 already in use
- Configuration file missing
- Network interfaces not ready

## How to Fix
1. Check smbd status
```bash
sudo systemctl status smbd
journalctl -u smbd -n 30
```
2. Validate config
```bash
testparm -s
```
3. Check for port conflicts
```bash
sudo ss -tlnp | grep :445
```

## Examples
```bash
$ sudo systemctl status smbd
● smbd.service - Samba SMB Daemon
   Active: failed (Result: exit-code)

$ journalctl -u smbd
smbd[1234]: [2023/03/15 10:00:00] ERROR: pid 1234 cant
