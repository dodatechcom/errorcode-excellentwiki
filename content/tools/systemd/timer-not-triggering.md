---
title: "[Solution] systemd timer not triggering"
description: "Fix systemd timer not triggering. Resolve timer units that are active but not starting their service."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd timer not triggering

## Error Description

myapp.timer: Timer is active but myapp.service has not been started.

The timer is running but not triggering its associated service.

## Common Causes

Common Causes:
- The associated service unit name does not match the timer name
- Timer is configured but the OnCalendar= expression has not yet matched
- The service unit is masked or has a dependency failure

## How to Fix

How to Fix:
```bash
# Verify timer-service name match
systemctl list-timers

# Check what the timer will start
systemctl list-dependencies myapp.timer

# Test the calendar expression
systemd-analyze calendar 'daily' --iterations=5

# Manually trigger the service
sudo systemctl start myapp.service
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