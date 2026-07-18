---
title: "[Solution] macOS WiFi No Internet — Connected But No Internet Access"
description: "Fix macOS WiFi no internet: connected to WiFi but no internet access, WiFi has no internet warning, pages won't load."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 161
---

# WiFi No Internet — Connected But No Internet Access

Fix macOS WiFi no internet: connected to WiFi but no internet access, WiFi has no internet warning, pages won't load.

## Common Causes

- DNS server not responding or misconfigured
- Router not providing internet connectivity
- DHCP lease expired and not renewed properly
- ISP service outage or router firmware issue

## How to Fix

### 1. Check Network Connectivity

```bash
ping -c 3 8.8.8.8
ping -c 3 google.com
networksetup -getinfo Wi-Fi
```

### 2. Fix DNS Settings

```bash
sudo networksetup -setdnsservers Wi-Fi 8.8.8.8 8.8.4.4
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

### 3. Renew DHCP Lease

```bash
sudo ipconfig set en0 DHCP
# Or System Settings → Network → WiFi → Details → TCP/IP → Renew DHCP Lease
```

### 4. Restart Network Services

```bash
sudo ifconfig en0 down && sudo ifconfig en0 up
sudo networksetup -setairportpower en0 off
sudo networksetup -setairportpower en0 on
```

## Common Scenarios

This error commonly occurs when:

- WiFi shows connected with full signal but websites won't load
- WiFi status shows 'No Internet Connection' warning
- Internet works on other devices but not on this Mac
- WiFi stops working intermittently requiring reconnect

## Prevent It

- Configure reliable public DNS servers (8.8.8.8, 1.1.1.1)
- Keep router firmware updated to fix DHCP renewal issues
- Restart Mac and router if internet stops working
- Check ISP status page before troubleshooting Mac network settings
