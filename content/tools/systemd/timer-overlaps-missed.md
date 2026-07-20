---
title: "[Solution] systemd timer overlaps missed"
description: "Fix systemd timer overlaps missed. Resolve timer execution gaps when runs overlap."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd timer overlaps missed

## Error Description

myapp.timer: Missed scheduled run. Timer interval too short.

The timer could not complete the previous run before the next one was due.

## Common Causes

Common Causes:
- Timer interval is shorter than the service execution time
- OnUnitActiveSec is too short
- System was under heavy load during the timer run

## How to Fix

How to Fix:
```bash
# Increase the timer interval
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnUnitActiveSec=2h
# Ensure this is longer than the service typically takes
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