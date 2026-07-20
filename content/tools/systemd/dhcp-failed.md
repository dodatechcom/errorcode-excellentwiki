---
title: "[Solution] systemd DHCP failed"
description: "Fix systemd DHCP failed. Resolve DHCP client failures with systemd-networkd."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd DHCP failed

## Error Description

eth0: DHCP lease failed. Could not obtain IP address.

The DHCP client could not obtain an IP address.

## Common Causes

Common Causes:
- DHCP server is unreachable
- Network cable is disconnected
- Network interface is down
- Firewall blocking DHCP traffic

## How to Fix

How to Fix:
```bash
# Check network status
networkctl status eth0

# Request DHCP lease manually
sudo networkctl renew eth0

# Check DHCP configuration
cat /etc/systemd/network/10-eth0.network

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