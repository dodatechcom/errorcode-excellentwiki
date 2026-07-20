---
title: "[Solution] systemd TimeoutStopSec too low"
description: "Fix systemd TimeoutStopSec too low errors. Resolve service stop timeouts when the grace period is insufficient."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd TimeoutStopSec too low

## Error Description

myapp.service: Stopping too quick, skipping ExecStop. Service stop request timed out.

The service did not stop within the configured TimeoutStopSec.

## Common Causes

Common Causes:
- TimeoutStopSec is too low for the application's shutdown time
- Application does not handle SIGTERM properly
- Application is waiting for in-flight requests to complete

## How to Fix

How to Fix:
```bash
# Increase the timeout
sudo systemctl edit myapp
```

```ini
[Service]
ExecStart=/usr/bin/myapp
ExecStop=/bin/kill -TERM $MAINPID
TimeoutStopSec=120
KillMode=mixed
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