---
title: "Ubuntu Unattended Upgrades Error"
description: "Automatic security updates fail or cause issues"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Unattended Upgrades Error

Automatic security updates fail or cause issues

## Common Causes

- Unattended-upgrades service not running
- Package held back preventing upgrade
- Insufficient disk space for upgrades
- Configuration syntax error in 50unattended-upgrades

## How to Fix

1. Check status: `systemctl status unattended-upgrades`
2. Check logs: `journalctl -u unattended-upgrades`
3. Test run: `sudo unattended-upgrades --dry-run --debug`
4. Review config: `cat /etc/apt/apt.conf.d/50unattended-upgrades`

## Examples

```bash
# Check unattended-upgrades status
systemctl status unattended-upgrades

# Test upgrade process
sudo unattended-upgrades --dry-run --debug

# Check logs
journalctl -u unattended-upgrades -n 50
```
