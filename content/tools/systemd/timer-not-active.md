---
title: "[Solution] systemd timer not active"
description: "Fix systemd timer not active errors. Resolve timer units that are not triggering their associated services."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd timer not active

## Error Description

myapp.timer: Timer is not active.

The timer unit is not in the active state and is not scheduling runs.

## Common Causes

Common Causes:
- Timer unit is not enabled
- Timer was stopped or failed
- Timer configuration has invalid calendar or monotonic value
- The associated service does not exist

## How to Fix

How to Fix:
```bash
# Check timer status
systemctl status myapp.timer

# Enable and start the timer
sudo systemctl enable myapp.timer
sudo systemctl start myapp.timer

# List all active timers
systemctl list-timers --all

# Check the timer configuration
systemctl cat myapp.timer
```

## Examples

```bash
# Check systemd version
systemctl --version

# Verify unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Analyze system boot
systemd-analyze blame

# List failed units
systemctl --failed

# View service logs
journalctl -u myapp -n 50 --no-pager
```