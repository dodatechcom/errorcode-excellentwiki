---
title: "[Solution] systemd basic.target not reached"
description: "Fix systemd basic.target not reached. Resolve boot failures when basic.target cannot be started."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd basic.target not reached

## Error Description

basic.target: Failed to start. Boot process incomplete.

The basic.target (system startup complete) could not be reached.

## Common Causes

Common Causes:
- A dependency of basic.target failed
- Socket units failed to start
- Timer units failed
- Slice or scope creation failed

## How to Fix

How to Fix:
```bash
# Check which basic.target deps failed
systemctl list-dependencies basic.target

# Check failed units
systemctl --failed

# Analyze boot time
systemd-analyze blame

# Check specific failures
journalctl -b -u <failed-unit>
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