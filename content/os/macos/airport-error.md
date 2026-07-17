---
title: "[Solution] macOS Wi-Fi / AirPort Errors"
description: "Fix macOS Wi-Fi and AirPort errors. Causes and solutions for wireless network connection and configuration failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# macOS Wi-Fi / AirPort Errors

Wi-Fi and AirPort errors indicate failures in wireless network connectivity, ranging from association failures to configuration issues. These errors affect system Wi-Fi, AirDrop, and Bonjour services.

## What This Error Means

Common Wi-Fi error states:

- `-3905` — Wi-Fi not associated with any network
- `-3906` — Wi-Fi network not found
- `-3912` — Wi-Fi hardware not available
- `ENOLINK (64)` — Network link is down

## Common Causes

- Wi-Fi hardware is turned off or in airplane mode
- Network password has changed since last connection
- Wi-Fi channel congestion or interference
- Driver or firmware issue with the wireless adapter

## How to Fix

### Check Wi-Fi Status

```bash
# Check Wi-Fi interface
networksetup -getairportnetwork en0

# List available networks
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s
```

### Reset Wi-Fi Connection

```bash
# Turn Wi-Fi off and on
networksetup -setairportpower en0 off
sleep 3
networksetup -setairportpower en0 on

# Rejoin specific network
networksetup -setairportnetwork en0 "SSID" "password"
```

### Reset Network Configuration

```bash
# Delete Wi-Fi preferences
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.wifi.message-tracer.plist
sudo rm -f /Library/Preferences/SystemConfiguration/NetworkInterfaces.plist

# Restart networking
sudo ifconfig en0 down && sudo ifconfig en0 up
```

### Forget and Re-add Network

```bash
# Remove known network
networksetup -removepreferrednetwork en0 "NetworkName"
```

## Related Errors

- [NSURLError]({{< relref "/os/macos/nsurlerror" >}}) — Network connection errors caused by Wi-Fi failures
- [Bonjour Service Discovery Errors]({{< relref "/os/macos/bonjour-error" >}}) — Service discovery failures on wireless networks
- [Core Foundation Errors]({{< relref "/os/macos/core-foundation" >}}) — Low-level networking errors
