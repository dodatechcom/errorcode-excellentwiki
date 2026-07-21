---
title: "Cron Daemon Not Running"
description: "Cron service (cron daemon) is not running on the system"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Cron Daemon Not Running

Cron service (cron daemon) is not running on the system

## Common Causes

- cron service stopped or crashed
- systemd disabled cron service
- Cron package not installed
- Alternative scheduler (systemd timers) replacing cron

## How to Fix

1. Check status: `systemctl status cron`
2. Start cron: `sudo systemctl start cron`
3. Enable on boot: `sudo systemctl enable cron`
4. Check if cron is installed: `dpkg -l | grep cron`

## Examples

```bash
# Check cron status
systemctl status cron

# Start and enable cron
sudo systemctl start cron
sudo systemctl enable cron

# Check if cron package is installed
dpkg -l | grep cron
```
