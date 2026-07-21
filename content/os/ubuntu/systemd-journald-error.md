---
title: "[Solution] Ubuntu Server: system-journald-error"
description: "Fix Ubuntu system-journald-error. systemd-journald fails to write or rotate logs."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Journald Error

systemd-journald encounters errors writing or rotating logs.

## Common Causes
- Journal disk usage exceeded SystemMaxUse
- Filesystem is full
- Journal file corrupted
- Permission issue on journal directory

## How to Fix
1. Check journal disk usage
```bash
journalctl --disk-usage
```
2. Vacuum old logs
```bash
sudo journalctl --vacuum-size=500M
sudo journalctl --vacuum-time=7d
```
3. Configure journald limits
```bash
sudo nano /etc/systemd/journald.conf
SystemMaxUse=1G
SystemMaxFileSize=100M
```
4. Restart journald
```bash
sudo systemctl restart systemd-journald
```

## Examples
```bash
$ journalctl --disk-usage
Archived and active journals take up 2.3G in the file system.

$ sudo journalctl --vacuum-size=500M
Vacuuming done, freed 1.8G of archived journals from /var/log/journal/.
```
