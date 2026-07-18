---
title: "[Solution] macOS WiFi Error — WiFi Not Connecting or Dropping"
description: "Fix macOS WiFi error: Wi-Fi not connecting, WiFi drops frequently, cannot join network, WiFi icon grayed out."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 160
---

# WiFi Error — WiFi Not Connecting or Dropping

Fix macOS WiFi error: Wi-Fi not connecting, WiFi drops frequently, cannot join network, WiFi icon grayed out.

## Common Causes

- WiFi preference files corrupted or misconfigured
- Wireless router firmware incompatible with Mac
- WiFi channel interference from neighboring networks
- Mac WiFi hardware antenna issue

## How to Fix

### 1. Check WiFi Status and Scan Networks

```bash
networksetup -getairportnetwork en0
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s
networksetup -listallhardwareports
```

### 2. Delete WiFi Preferences and Rejoin

```bash
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.wifi.message-tracer.plist
sudo shutdown -r now
```

### 3. Create New WiFi Location

```bash
# System Settings → Network → WiFi → Locations → Edit Locations → Add
# Set 'Location' to 'Automatic' or create new custom location
```

### 4. Reset Network Settings Completely

```bash
sudo rm -f /Library/Preferences/SystemConfiguration/NetworkInterfaces.plist
sudo rm -f /Library/Preferences/SystemConfiguration/preferences.plist
sudo shutdown -r now
```

## Common Scenarios

This error commonly occurs when:

- Mac cannot join WiFi network that other devices connect to fine
- WiFi connection drops several times per day requiring reconnection
- WiFi icon shows in menu bar but no networks appear in list
- WiFi connected but with yellow dot and no internet access

## Prevent It

- Keep WiFi router firmware updated for macOS compatibility
- Avoid placing Mac near microwaves or Bluetooth devices on 2.4GHz
- Use 5GHz WiFi band for less interference in crowded areas
- Restart Mac and router periodically to clear connection state
