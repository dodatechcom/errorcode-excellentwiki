---
title: "[Solution] systemd network-online.target timeout"
description: "Fix systemd network-online.target timeout. Resolve boot delays when waiting for network availability."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd network-online.target timeout

## Error Description

network-online.target: Job timed out. Network not ready within timeout.

The network did not become available within the expected time.

## Common Causes

Common Causes:
- Network interface is slow to get an IP address
- DHCP server is unreachable
- NetworkManager or systemd-networkd not configured
- Waiting for a specific interface that does not exist

## How to Fix

How to Fix:
```bash
# Check network status
systemctl status NetworkManager
# or
systemctl status systemd-networkd

# Configure network wait
sudo systemctl edit network-online.target
```

```ini
[Unit]
DefaultTimeoutStartSec=120
```

```bash
# For systemd-networkd, check configuration
networkctl status
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