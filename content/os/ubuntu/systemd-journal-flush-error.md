---
title: "Systemd Journal Flush Error"
description: "Journal files fail to flush to persistent storage"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd Journal Flush Error

Journal files fail to flush to persistent storage

## Common Causes

- Storage directory not writable
- Disk full preventing journal flush
- Journal size exceeds SystemMaxUse limit
- Filesystem permissions wrong on /var/log/journal/

## How to Fix

1. Check journal location: `journalctl --disk-usage`
2. Flush manually: `sudo journalctl --flush`
3. Check permissions: `ls -la /var/log/journal/`
4. Vacuum: `sudo journalctl --vacuum-size=100M`

## Examples

```bash
# Check journal disk usage
journalctl --disk-usage

# Flush journal to disk
sudo journalctl --flush

# Check journal directory
ls -la /var/log/journal/
```
