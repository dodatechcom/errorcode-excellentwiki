---
title: "NetworkManager DNS Plugin Error"
description: "NetworkManager DNS resolution not working with plugins"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# NetworkManager DNS Plugin Error

NetworkManager DNS resolution not working with plugins

## Common Causes

- DNS plugin (dnsmasq, systemd-resolved) not installed
- Plugin configuration conflicts with /etc/resolv.conf
- Multiple DNS plugins active simultaneously
- Plugin crashed or not responding

## How to Fix

1. Check plugins: `nmcli general`
2. Check DNS: `nmcli dev show | grep DNS`
3. Restart NetworkManager: `sudo systemctl restart NetworkManager`
4. Check plugin config: `cat /etc/NetworkManager/NetworkManager.conf`

## Examples

```bash
# Check NetworkManager status
nmcli general status

# Check DNS configuration
nmcli dev show | grep DNS

# Check NetworkManager config
cat /etc/NetworkManager/NetworkManager.conf
```
