---
title: "[Solution] systemd memory pressure action"
description: "Fix systemd memory pressure action. Resolve unexpected behavior from MemoryPressureAction settings."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd memory pressure action

## Error Description

myapp.service: MemoryPressureAction=kill triggered. Service terminated.

The service was killed due to memory pressure events.

## Common Causes

Common Causes:
- MemoryPressureAction is set to 'kill'
- System is under sustained memory pressure
- Service does not handle memory pressure gracefully
- Action threshold is too sensitive

## How to Fix

How to Fix:
```bash
# Change the action to 'none' or 'log'
sudo systemctl edit myapp
```

```ini
[Service]
MemoryPressureAction=log
# Options: none, log, kill, watch
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