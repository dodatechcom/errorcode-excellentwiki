---
title: "Systemd Journald High Disk Usage"
description: "journald consuming excessive disk space due to log retention"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd Journald High Disk Usage

journald consuming excessive disk space due to log retention

## Common Causes

- SystemMaxUse not configured or too high
- Persistent logging enabled storing all logs
- High verbosity logging from applications
- Log rotation not happening due to timer failure

## How to Fix

1. Check usage: `journalctl --disk-usage`
2. Vacuum old logs: `sudo journalctl --vacuum-size=500M`
3. Configure limits: edit /etc/systemd/journald.conf
4. Restart journald: `sudo systemctl restart systemd-journald`

## Examples

```bash
# Check journald disk usage
journalctl --disk-usage

# Limit journal to 500MB
sudo journalctl --vacuum-size=500M

# Configure persistent limit
sudo sed -i 's/#SystemMaxUse=/SystemMaxUse=500M/' /etc/systemd/journald.conf
sudo systemctl restart systemd-journald
```
