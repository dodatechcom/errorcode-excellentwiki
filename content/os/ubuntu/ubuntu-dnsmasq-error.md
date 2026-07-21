---
title: "Ubuntu Dnsmasq Error"
description: "Dnsmasq DNS/DHCP service fails to start or serve requests"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Dnsmasq Error

Dnsmasq DNS/DHCP service fails to start or serve requests

## Common Causes

- Port 53 already in use by another service (systemd-resolved)
- Configuration syntax error in /etc/dnsmasq.conf
- DHCP range overlaps with static assignments
- Lease file permissions incorrect

## How to Fix

1. Check status: `systemctl status dnsmasq`
2. Test config: `dnsmasq --test`
3. Check port conflict: `sudo ss -tlnp | grep :53`
4. Review logs: `journalctl -u dnsmasq`

## Examples

```bash
# Check dnsmasq status
systemctl status dnsmasq

# Test configuration
sudo dnsmasq --test

# Check what's using port 53
sudo ss -tlnp | grep :53
```
