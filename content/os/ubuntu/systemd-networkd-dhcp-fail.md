---
title: "Systemd-networkd DHCP Failure"
description: "systemd-networkd cannot obtain IP address via DHCP"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd-networkd DHCP Failure

systemd-networkd cannot obtain IP address via DHCP

## Common Causes

- DHCP client not enabled in .network file
- Network interface not managed by systemd-networkd
- DHCP server not responding
- Resolv.conf not pointing to systemd-resolved

## How to Fix

1. Check network files: `ls /etc/systemd/network/`
2. Enable DHCP: add `DHCP=yes` to [Network] section
3. Restart networkd: `sudo systemctl restart systemd-networkd`
4. Check status: `networkctl status`

## Examples

```bash
# Check network files
ls /etc/systemd/network/

# Check networkctl status
networkctl status

# Restart networkd
sudo systemctl restart systemd-networkd
```
