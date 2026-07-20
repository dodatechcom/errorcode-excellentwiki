---
title: "[Solution] systemd resolved stub listener conflict"
description: "Fix systemd resolved stub listener conflict. Resolve DNS listener port conflicts with systemd-resolved."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd resolved stub listener conflict

## Error Description

systemd-resolved: Failed to listen on stub DNS listener: Address already in use

Another process is using port 53.

## Common Causes

Common Causes:
- dnsmasq or another DNS server is using port 53
- Multiple instances of systemd-resolved
- dnsmasq is not stopped before enabling resolved

## How to Fix

How to Fix:
```bash
# Find what is using port 53
sudo ss -ulnp | grep :53

# Stop conflicting DNS servers
sudo systemctl stop dnsmasq
sudo systemctl disable dnsmasq

# Enable and start resolved
sudo systemctl enable systemd-resolved
sudo systemctl start systemd-resolved
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