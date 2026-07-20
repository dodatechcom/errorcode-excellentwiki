---
title: "[Solution] systemd reload not supported"
description: "Fix systemd reload not supported errors. Resolve reload failures for services without ExecReload."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd reload not supported

## Error Description

Failed to reload myapp.service: Service does not support reload operation.

No ExecReload= is defined for this service.

## Common Causes

Common Causes:
- ExecReload is not defined in the unit file
- Service uses Type=simple without ExecReload
- Application does not support config reload

## How to Fix

How to Fix:
```bash
# Check if ExecReload is defined
grep ExecReload /etc/systemd/system/myapp.service

# Add ExecReload to the unit
sudo systemctl edit myapp
```

```ini
[Service]
Type=simple
ExecStart=/usr/bin/myapp --config /etc/myapp/config.yml
ExecReload=/bin/kill -HUP $MAINPID
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