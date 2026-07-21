---
title: "[Solution] Ubuntu Server: system-journald-corrupt"
description: "Fix Ubuntu system-journald-corrupt. Journal files are corrupted and unreadable."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Journald Corrupt

Journal files are corrupted making logs unreadable.

## Common Causes
- System crash during journal write
- Disk failure corrupting journal files
- Power loss mid-write
- Journal file truncated

## How to Fix
1. Check for corrupted journal files
```bash
ls -la /var/log/journal/
```
2. Remove corrupted journal files
```bash
sudo rm /var/log/journal/*.journal
sudo rm /var/log/journal/*/*.journal
```
3. Restart journald
```bash
sudo systemctl restart systemd-journald
```

## Examples
```bash
$ journalctl -b
Failed to add inotify watch for journal file: Bad message

$ sudo rm /var/log/journal/remote/*.journal*
$ sudo systemctl restart systemd-journald
$ journalctl -b
-- Logs begin at Mon 2023-01-01 10:00:00 UTC --
```
