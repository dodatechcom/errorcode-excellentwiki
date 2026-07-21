---
title: "[Solution] Linux: systemd-journal-corrupt -- journal files corrupted"
description: "Fix Linux systemd journal corruption errors. Systemd journal files corrupted and unreadable."
os: ["linux"]
error-types: ["systemd-error"]
severities: ["error"]
---

# Linux: Systemd Journal Corruption

Systemd journal corruption occurs when journal files become damaged or unreadable.

## Common Causes

- Power failure during journal write
- Disk full causing incomplete journal entries
- Filesystem corruption affecting journal directory
- Journal size exceeding configured limit
- Incompatible journal format after upgrade

## How to Fix

### 1. Check Journal Status

```bash
journalctl --disk-usage
journalctl --verify
ls -la /var/log/journal/
```

### 2. Vacuum Old Journals

```bash
sudo journalctl --vacuum-size=100M
sudo journalctl --vacuum-time=7d
```

### 3. Rebuild Journal

```bash
sudo journalctl --rotate
sudo journalctl --vacuum-size=50M
sudo rm -rf /var/log/journal/*
sudo systemd-tmpfiles --create
```

## Examples

```bash
$ journalctl --verify
PASS: /var/log/journal/abc123/system.journal
FAIL: /var/log/journal/abc123/user-1000.journal: File corrupt
$ sudo journalctl --vacuum-size=100M
Vacuuming done, freed 256M of archived journals on disk.
```
