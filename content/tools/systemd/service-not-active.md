---
title: "[Solution] systemd service not active"
description: "Fix systemd service not active errors. Resolve issues where a service is not in the active state."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd service not active

## Error Description

myapp.service: Unit is not active.

The service is not currently running.

## Common Causes

Common Causes:
- Service was never started
- Service crashed and was not set to restart
- Service was manually stopped
- Dependency failure prevented start

## How to Fix

How to Fix:
```bash
# Check service state
systemctl is-active myapp
systemctl status myapp

# Start the service
sudo systemctl start myapp

# Enable on boot
sudo systemctl enable myapp

# Check why it failed
journalctl -u myapp -n 50 --no-pager
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