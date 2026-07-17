---
title: "[Solution] macOS Wi-Fi Connection Error"
description: "Fix macOS Wi-Fi not connecting, dropping, or showing 'no Internet' errors. Resolve Wi-Fi issues on Mac with proven troubleshooting steps."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["wifi", "network", "connection", "internet", "wireless"]
weight: 5
---

# macOS Wi-Fi Connection Error Fix

Wi-Fi errors on macOS manifest as inability to connect, frequent disconnections, slow speeds, or "No Internet" warnings despite being connected to a network.

## What This Error Means

macOS Wi-Fi issues can stem from software configuration problems, interference, or hardware faults. The Wi-Fi menu bar icon may show full bars but no Internet access, or the network may fail to join entirely.

## Common Causes

- Corrupt Wi-Fi preference files
- DNS configuration issues
- Router compatibility problems (band, security type)
- Interference from other wireless devices
- macOS Wi-Fi bug after update
- Incorrect date/time preventing WPA2/WPA3 authentication

## How to Fix

### 1. Renew DHCP lease

```bash
# Release and renew IP address
sudo ipconfig set en0 DHCP

# Or via networksetup
sudo networksetup -setdhcp Wi-Fi
```

### 2. Delete Wi-Fi preferences and reconnect

```bash
# Turn off Wi-Fi first from System Preferences
# Delete corrupt preference files
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist
sudo rm -f /Library/Preferences/SystemConfiguration/NetworkInterfaces.plist
sudo rm -f /Library/Preferences/SystemConfiguration/preferences.plist

# Restart the Mac and reconnect to Wi-Fi
```

### 3. Flush DNS cache

```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

### 4. Set custom DNS servers

```bash
# Use Google DNS or Cloudflare
sudo networksetup -setdnsservers Wi-Fi 8.8.8.8 8.8.4.4

# Or use Cloudflare
sudo networksetup -setdnsservers Wi-Fi 1.1.1.1 1.0.0.1
```

### 5. Create a new Wi-Fi network location

```bash
# Open System Preferences → Network → Wi-Fi → Locations → Edit Locations
# Click "+" to add a new location
# Reconnect to your Wi-Fi network
```

## Related Errors

- [Bonjour Error](bonjour-error) — network service discovery issues
- [NSURL Error](nsurlerror) — network connection errors in apps
- [Airport Error](airport-error) — Wi-Fi hardware errors
