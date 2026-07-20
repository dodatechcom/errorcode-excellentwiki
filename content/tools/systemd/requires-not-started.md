---
title: "[Solution] systemd Requires not started"
description: "Fix systemd Requires not started. Resolve service failures when a Required dependency fails to start."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd Requires not started

## Error Description

myapp.service: Requires=database.service was not started.

The service requires database.service which is not running.

## Common Causes

Common Causes:
- The required unit failed to start
- The required unit is masked
- The required unit is not installed
- Dependency is too strict for the use case

## How to Fix

How to Fix:
```bash
# Check the required unit
systemctl status database.service

# Start it manually
sudo systemctl start database.service

# Consider using Wants= instead of Requires= for optional dependencies
sudo systemctl edit myapp
```

```ini
[Unit]
Wants=database.service
After=database.service
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