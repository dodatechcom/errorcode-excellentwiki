---
title: "[Solution] Linux: cron-overflow-error -- cron spool overflow"
description: "Fix Linux cron overflow errors. Cron spool overflow or too many scheduled jobs."
os: ["linux"]
error-types: ["cron-error"]
severities: ["warning"]
---

# Linux: Cron Overflow Error

Cron overflow occurs when the cron spool fills up or too many jobs are scheduled.

## Common Causes

- Thousands of user crontab files in /var/spool/cron
- Single crontab exceeding maximum line limit
- cron.{allow,deny} files preventing entries
- /var/spool/cron partition full
- Cron daemon unable to process queue

## How to Fix

### 1. Check Cron Queue

```bash
ls -la /var/spool/cron/crontabs/ | wc -l
ls -la /var/spool/cron/ | wc -l
```

### 2. Clean Old Entries

```bash
sudo find /var/spool/cron/crontabs/ -mtime +30 -ls
sudo crontab -r -u olduser
```

### 3. Check Disk Usage

```bash
df -h /var/spool/cron
du -sh /var/spool/cron/*
sudo systemctl restart cron
```

## Examples

```bash
$ ls /var/spool/cron/crontabs/ | wc -l
2847
$ df -h /var/spool/cron
Filesystem  Size  Used  Avail  Use%
/dev/sda1   50G   48G   2G    96%
```
