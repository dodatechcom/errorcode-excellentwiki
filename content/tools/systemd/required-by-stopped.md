---
title: "[Solution] systemd required by stopped unit"
description: "Fix systemd required by stopped unit. Resolve service start issues when a RequiredBy= target or service is stopped."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd required by stopped unit

## Error Description

myapp.service is required by some-unit.service, which is stopped.

Starting myapp may not be useful as its consumer is not running.

## Common Causes

Common Causes:
- The unit listing myapp as RequiredBy= is not running
- The requiring unit was manually stopped
- The dependency graph is inverted

## How to Fix

How to Fix:
```bash
# Check which units require myapp
systemctl list-dependencies --reverse myapp

# Start the requiring unit if needed
sudo systemctl start some-unit

# Or adjust dependencies
sudo systemctl edit myapp
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