---
title: "[Solution] systemd LimitNOFILE too low"
description: "Fix systemd LimitNOFILE too low errors. Resolve service failures when the open file descriptor limit is insufficient."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd LimitNOFILE too low

## Error Description

myapp.service: Failed to adjust resource limits: Too many open files

The LimitNOFILE value is too low for the application.

## Common Causes

Common Causes:
- Default LimitNOFILE is 1024 which is too low for high-concurrency apps
- Application opens many connections or file descriptors
- The system-wide limit (ulimit -n) is lower than the configured value

## How to Fix

How to Fix:
```bash
# Check current limits
systemctl show myapp | grep LimitNOFILE
cat /proc/$(pidof myapp)/limits | grep "Max open files"

# Increase in the unit file
sudo systemctl edit myapp
```

```ini
[Service]
ExecStart=/usr/bin/myapp
LimitNOFILE=65536
LimitNPROC=65536
```

```bash
# Also set system-wide
echo "fs.file-max = 2097152" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
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