---
title: "[Solution] systemd ExecStop not defined"
description: "Fix systemd ExecStop not defined warnings. Resolve graceful shutdown issues when ExecStop is missing."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd ExecStop not defined

## Error Description

Warning: myapp.service: ExecStop= is not set. Using default stop signal.

Without ExecStop, systemd sends SIGTERM by default. Custom stop behavior requires an explicit ExecStop.

## Common Causes

Common Causes:
- ExecStop was not set and default SIGTERM is insufficient
- Application needs a specific shutdown command
- Service requires cleanup before stopping

## How to Fix

How to Fix:
```bash
# Add ExecStop to the unit file
sudo systemctl edit myapp
```

Example with ExecStop:
```ini
[Service]
Type=simple
ExecStart=/usr/bin/myapp
ExecStop=/usr/bin/myapp --stop
KillSignal=SIGTERM
TimeoutStopSec=30
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