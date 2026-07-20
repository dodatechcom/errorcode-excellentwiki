---
title: "[Solution] systemd After dependency not met"
description: "Fix systemd After dependency not met. Resolve service ordering failures when After= dependencies are not satisfied."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd After dependency not met

## Error Description

myapp.service: After dependency network-online.target was not started.

The service requires network-online.target to be started first.

## Common Causes

Common Causes:
- The After= dependency unit is not enabled or not installed
- The dependency unit failed to start
- Incorrect ordering dependency

## How to Fix

How to Fix:
```bash
# Check if the dependency is enabled
systemctl is-enabled network-online.target

# Enable the dependency
sudo systemctl enable network-online.target

# Use Wants= along with After= for soft dependencies
sudo systemctl edit myapp
```

```ini
[Unit]
After=network-online.target
Wants=network-online.target
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