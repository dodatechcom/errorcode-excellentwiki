---
title: "[Solution] macOS Kernel Panic WiFi — Wireless Driver Crash"
description: "Fix macOS kernel panic triggered by Wi-Fi: system restarts when connecting to wireless networks, WiFi kext panic in logs."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 94
---

# Kernel Panic WiFi — Wireless Driver Crash

Fix macOS kernel panic triggered by Wi-Fi: system restarts when connecting to wireless networks, WiFi kext panic in logs.

## Common Causes

- Faulty Wi-Fi card or antenna connection inside the Mac
- Corrupted Wi-Fi kext or preferences from macOS update
- Interference from USB 3.0 devices on 2.4GHz band
- Third-party Wi-Fi adapter with incompatible driver

## How to Fix

### 1. Check WiFi Panic Logs

```bash
log show --predicate 'eventMessage contains "wifi"' --last 24h | grep -i panic
system_profiler SPAirPortDataType
ifconfig en0 | grep -i status
```

### 2. Reset WiFi Preferences

```bash
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.wifi.message-tracer.plist
sudo shutdown -r now
```

### 3. Switch WiFi Band

```bash
# System Settings → WiFi → Connect to 5GHz network instead of 2.4GHz
```

### 4. Update macOS and WiFi Firmware

```bash
softwareupdate -l
softwareupdate -i -a
```

## Common Scenarios

This error commonly occurs when:

- Kernel panic occurs immediately when Wi-Fi is turned on
- Panic log references AppleBCMWLANCore or IO80211Family
- Mac crashes when switching between Wi-Fi networks
- Kernel panic happens when USB 3.0 hub is connected near Wi-Fi

## Prevent It

- Use 5GHz Wi-Fi band to avoid USB 3.0 interference on 2.4GHz
- Keep macOS updated to get latest WiFi driver fixes
- Remove third-party WiFi adapters if they cause recurring panics
- Avoid placing USB 3.0 devices near the Mac WiFi antenna
