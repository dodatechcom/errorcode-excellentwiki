---
title: "[Solution] systemd OOM killed by systemd-oomd"
description: "Fix systemd OOM kill by systemd-oomd. Resolve services killed by the systemd OOM daemon."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd OOM killed by systemd-oomd

## Error Description

myapp.service: Killed by systemd-oomd due to memory pressure.

systemd-oomd killed the service because system memory pressure was too high.

## Common Causes

Common Causes:
- System is under heavy memory pressure
- Memory limits are too generous for the workload
- systemd-oomd is aggressively killing processes
- ManagedOOMMemoryPressure is set to kill

## How to Fix

How to Fix:
```bash
# Check oomd status
systemctl status systemd-oomd

# Adjust oomd settings
sudo systemctl edit systemd-oomd
```

```ini
[Service]
ManagedOOMMemoryPressure=kill
ManagedOOMSwap=kill
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