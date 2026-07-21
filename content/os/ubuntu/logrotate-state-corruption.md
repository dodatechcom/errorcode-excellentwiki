---
title: "Logrotate State File Corruption"
description: "Logrotate state file corrupted causing repeated or skipped rotations"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Logrotate State File Corruption

Logrotate state file corrupted causing repeated or skipped rotations

## Common Causes

- State file /var/lib/logrotate/status corrupted
- Multiple logrotate processes running simultaneously
- Disk full during state file write
- Manual editing of state file caused syntax error

## How to Fix

1. Check state: `cat /var/lib/logrotate/status`
2. Delete state: `sudo rm /var/lib/logrotate/status` (will recreate on next run)
3. Run logrotate: `sudo logrotate /etc/logrotate.conf`
4. Verify rotation: `ls -la /var/log/*.gz`

## Examples

```bash
# Check logrotate state
head -20 /var/lib/logrotate/status

# Reset state file
sudo rm /var/lib/logrotate/status
sudo logrotate /etc/logrotate.conf

# Verify rotations happened
ls -la /var/log/syslog*
```
