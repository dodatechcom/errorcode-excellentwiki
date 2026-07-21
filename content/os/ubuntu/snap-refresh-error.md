---
title: "[Solution] Ubuntu Server: snap-refresh-error"
description: "Fix Ubuntu snap-refresh-error. snap refresh fails due to network or disk space issues."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Snap Refresh Error

snapd cannot update installed snaps.

## Common Causes
- Network connectivity lost during refresh
- New snap version incompatible
- snapd daemon not responding
- Insufficient space in /var/lib/snapd

## How to Fix
1. Check snapd logs
```bash
journalctl -u snapd -n 50
```
2. Force refresh
```bash
sudo snap refresh --list
sudo snap refresh <package> --classic
```
3. Reset snapd if needed
```bash
sudo systemctl restart snapd
```

## Examples
```bash
$ sudo snap refresh
error: cannot refresh: snap has running apps (nextcloud)

$ sudo snap stop nextcloud
$ sudo snap refresh
```
