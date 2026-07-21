---
title: "[Solution] macOS WiFi Keeps Disconnecting -- Mac WiFi Drops Repeatedly"
description: "Fix macOS WiFi keeps disconnecting when Mac WiFi drops intermittently. Resolve WiFi disconnecting issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS WiFi Keeps Disconnecting -- Mac WiFi Drops Repeatedly

When your Mac's WiFi connection drops repeatedly, you may see the WiFi icon change from connected to not connected, or applications lose their network connection.

## Common Causes
- WiFi router is overloaded or has a weak signal
- macOS WiFi settings are corrupted
- Power management is putting the WiFi radio to sleep
- Channel conflict with neighboring networks
- Router firmware is outdated or buggy

## How to Fix
1. Delete the WiFi preference files and reconnect
2. Disable WiFi power saving in terminal
3. Change the WiFi channel on your router to a less congested one
4. Update router firmware
5. Reset the Mac's network configuration entirely

```bash
# Delete corrupted WiFi preferences
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.wifi.message-tracer.plist

# Restart the networking services
sudo ifconfig en0 down && sudo ifconfig en0 up
```

## Examples

```bash
# Monitor WiFi connection status
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I
```

This error is common when the WiFi router firmware has known issues, when macOS power management aggressively puts the WiFi radio to sleep, or when channel congestion causes periodic disconnections.
