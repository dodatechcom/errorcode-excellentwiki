---
title: "Systemd Journal Vacuum Configuration Error"
description: "Journal vacuum not cleaning old logs as expected"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd Journal Vacuum Configuration Error

Journal vacuum not cleaning old logs as expected

## Common Causes

- SystemMaxUse not set in journald.conf
- MaxRetentionSec limiting vacuum effectiveness
- Journal files sealed preventing removal
- Vacuum timer not running or disabled

## How to Fix

1. Check usage: `journalctl --disk-usage`
2. Vacuum by size: `sudo journalctl --vacuum-size=500M`
3. Vacuum by time: `sudo journalctl --vacuum-time=30d`
4. Configure: edit /etc/systemd/journald.conf and restart journald

## Examples

```bash
# Check journal disk usage
journalctl --disk-usage

# Vacuum to 200MB
sudo journalctl --vacuum-size=200M

# Vacuum logs older than 7 days
sudo journalctl --vacuum-time=7d
```
