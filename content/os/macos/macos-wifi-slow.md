---
title: "[Solution] macOS WiFi Slow -- Mac Has Slow WiFi Connection"
description: "Fix macOS WiFi slow connection when Mac has significantly slower WiFi than other devices. Resolve slow wireless speeds on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS WiFi Slow -- Mac Has Slow WiFi Connection

A slow WiFi connection on Mac can manifest as slow webpage loading, buffering videos, or speed tests showing much lower speeds than expected.

## Common Causes
- WiFi channel congestion from neighboring networks
- DNS server is slow or overloaded
- WiFi antenna is partially obstructed
- macOS is connected to a 2.4 GHz band instead of 5 GHz
- VPN or proxy adding latency to the connection

## How to Fix
1. Switch to the 5 GHz WiFi band for faster speeds
2. Change DNS servers to a fast public DNS (1.1.1.1 or 8.8.8.8)
3. Move closer to the WiFi router or remove obstructions
4. Disable any active VPN and test speed again
5. Reset the WiFi configuration and reconnect

```bash
# Check current WiFi connection details
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I

# Change DNS servers
networksetup -setdnsservers Wi-Fi 1.1.1.1 8.8.8.8
```

## Examples

```bash
# Test network speed
networkquality

# Check for WiFi interference
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s
```

This error commonly occurs in dense apartment buildings with channel congestion, when the Mac is far from the router, or when DNS resolution is adding significant latency.
