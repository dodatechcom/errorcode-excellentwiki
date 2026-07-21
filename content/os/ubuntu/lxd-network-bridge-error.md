---
title: "LXD Network Bridge Error"
description: "LXD network bridge fails to start or route traffic"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# LXD Network Bridge Error

LXD network bridge fails to start or route traffic

## Common Causes

- Network bridge interface not created
- dnsmasq service for LXD bridge not running
- IP forwarding not enabled
- Firewall rules blocking bridge traffic

## How to Fix

1. Check bridge status: `ip link show lxdbr0`
2. Verify dnsmasq: `systemctl status lxd-dnsmasq`
3. Enable IP forwarding: `sysctl net.ipv4.ip_forward=1`
4. Check LXD network: `lxc network show lxdbr0`

## Examples

```bash
# Check LXD network status
lxc network show lxdbr0

# Restart network bridge
lxc network restart lxdbr0

# Enable IP forwarding permanently
echo 'net.ipv4.ip_forward=1' | sudo tee /etc/sysctl.d/99-lxd.conf
sudo sysctl -p /etc/sysctl.d/99-lxd.conf
```
