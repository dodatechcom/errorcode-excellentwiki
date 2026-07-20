---
title: "[Solution] systemd link not ready"
description: "Fix systemd link not ready. Resolve network link state issues with systemd-networkd."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd link not ready

## Error Description

eth0: Link is not ready. Waiting for carrier.

The network link is down or waiting for carrier signal.

## Common Causes

Common Causes:
- Physical cable is disconnected
- Network interface is administratively down
- Switch port is disabled
- Driver issue with the NIC

## How to Fix

How to Fix:
```bash
# Check link status
networkctl status eth0

# Bring link up
sudo ip link set eth0 up

# Check physical connection
ethtool eth0

# Restart networkd
sudo systemctl restart systemd-networkd
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