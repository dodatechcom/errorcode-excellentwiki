---
title: "[Solution] systemd main process exited"
description: "Fix systemd main process exited errors. Resolve unexpected service termination when the main process stops."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd main process exited

## Error Description

myapp.service: Main process exited, code=exited, status=15/SIGTERM

The main process of the service was terminated unexpectedly.

## Common Causes

Common Causes:
- Process received a signal (SIGTERM, SIGKILL, etc.)
- OOM killer terminated the process
- Application crashed due to a bug
- The process was stopped by another service

## How to Fix

How to Fix:
```bash
# Check if OOM killed
dmesg | grep -i oom | tail -5
journalctl -u myapp -n 50 --no-pager

# Increase memory limits if OOM
sudo systemctl edit myapp
```

```ini
[Service]
MemoryMax=4G
MemoryHigh=3G
OOMPolicy=continue
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