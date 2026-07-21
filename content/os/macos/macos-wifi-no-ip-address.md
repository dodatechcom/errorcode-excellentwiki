---
title: "[Solution] macOS WiFi No IP Address -- Mac Not Getting IP from DHCP"
description: "Fix macOS WiFi no IP address when Mac cannot obtain an IP address from the DHCP server. Resolve WiFi connected but no IP on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS WiFi No IP Address -- Mac Not Getting IP from DHCP

When your Mac connects to WiFi but cannot obtain an IP address, the WiFi icon shows connected but you have no internet access. The Mac may show a self-assigned IP address (169.254.x.x).

## Common Causes
- DHCP server on the router is not responding
- Router has exhausted its DHCP address pool
- MAC address filtering is blocking the Mac
- WiFi security settings are mismatched
- Multiple devices are conflicting on the same IP

## How to Fix
1. Renew the DHCP lease from terminal
2. Restart the WiFi router and modem
3. Set a static IP address temporarily to test
4. Check router DHCP settings and address pool
5. Reset the Mac's network configuration

```bash
# Renew DHCP lease
sudo ipconfig set en0 DHCP

# Check current IP address
ifconfig en0 | grep inet

# Force a new DHCP request
sudo ipconfig set en0 INFORM 192.168.1.100 255.255.255.0
```

## Examples

```bash
# Check for self-assigned IP (169.254.x.x)
ifconfig en0 | grep "169.254"

# Release and renew DHCP
sudo ipconfig set en0 DHCP
```

This error is common when the router's DHCP pool is exhausted, when MAC address filtering is enabled and the Mac's address is not in the allowed list, or when the router needs a restart.
