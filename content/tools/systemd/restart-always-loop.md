---
title: "[Solution] systemd Restart=always loop"
description: "Fix systemd Restart=always loop. Resolve service restart loops where a service continuously crashes and restarts."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd Restart=always loop

## Error Description

myapp.service: Service entered restart loop with 5 restarts in 10 seconds. Stopping.

The service keeps crashing and systemd has hit the start rate limit.

## Common Causes

Common Causes:
- The application has a fatal error on startup
- Missing dependencies or configuration
- Incorrect ExecStart path or arguments
- Port conflict preventing startup

## How to Fix

How to Fix:
```bash
# Check recent logs
journalctl -u myapp -n 50 --no-pager

# Check restart rate limits
systemctl show myapp | grep -E 'StartLimit|RestartSec'

# Temporarily disable restart to debug
sudo systemctl edit myapp
# Add:
# [Service]
# Restart=on-failure
# StartLimitIntervalSec=600
# StartLimitBurst=5

# Fix the underlying issue
sudo myapp --test-config
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