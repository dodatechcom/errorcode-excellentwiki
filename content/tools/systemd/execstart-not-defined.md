---
title: "[Solution] systemd ExecStart not defined"
description: "Fix systemd ExecStart not defined errors. Resolve service start failures when ExecStart is missing from the unit file."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd ExecStart not defined

## Error Description

Failed to start myapp.service: Unit myapp.service has a bad unit file setting.

For service unit files of Type=simple, ExecStart= must be set.

## Common Causes

Common Causes:
- ExecStart directive is missing from the [Service] section
- The unit file is for a oneshot service without ExecStart
- The directive was commented out accidentally

## How to Fix

How to Fix:
```bash
# Check if ExecStart is defined
grep ExecStart /etc/systemd/system/myapp.service

# Edit the unit file to add ExecStart
sudo systemctl edit myapp --force
```

Example with ExecStart:
```ini
[Service]
Type=simple
ExecStart=/usr/bin/myapp --config /etc/myapp/config.yml
WorkingDirectory=/opt/myapp
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