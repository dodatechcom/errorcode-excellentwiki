---
title: "[Solution] Ubuntu Server: ubuntu-motd-error"
description: "Fix Ubuntu ubuntu-motd-error. Message of the day shows errors at login."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu MOTD Error

MOTD scripts fail showing errors at SSH login.

## Common Causes
- MOTD script has errors
- /etc/update-motd.d/ script failing
- Permissions wrong on MOTD scripts

## How to Fix
1. Check MOTD scripts
```bash
ls -la /etc/update-motd.d/
```
2. Test MOTD scripts
```bash
sudo run-parts /etc/update-motd.d/
```
3. Fix permissions
```bash
sudo chmod +x /etc/update-motd.d/*
```

## Examples
```bash
$ sudo run-parts /etc/update-motd.d/
/etc/update-motd.d/50-motd-news: line 10: curl: command not found
```