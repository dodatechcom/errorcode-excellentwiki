---
title: "UFW IPv6 Rules Not Working"
description: "UFW firewall rules not applied to IPv6 traffic"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# UFW IPv6 Rules Not Working

UFW firewall rules not applied to IPv6 traffic

## Common Causes

- IPv6 not enabled in UFW configuration
- ip6tables rules not loaded
- Network interface not configured for IPv6
- UFW IPv6 setting disabled in /etc/default/ufw

## How to Fix

1. Check IPv6 setting: `cat /etc/default/ufw | grep IPV6`
2. Enable IPv6: `sudo sed -i 's/IPV6=no/IPV6=yes/' /etc/default/ufw`
3. Reload UFW: `sudo ufw reload`
4. Check ip6tables: `sudo ip6tables -L -n`

## Examples

```bash
# Check if IPv6 is enabled in UFW
grep IPV6 /etc/default/ufw

# Enable IPv6
sudo sed -i 's/IPV6=no/IPV6=yes/' /etc/default/ufw
sudo ufw reload

# Check ip6tables rules
sudo ip6tables -L -n
```
