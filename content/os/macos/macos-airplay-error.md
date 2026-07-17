---
title: "[Solution] macOS AirPlay Not Working"
description: "Fix AirPlay errors on Mac when you can't stream to Apple TV, AirPlay icons are missing, or connections drop."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["airplay", "streaming", "apple-tv", "screen-mirroring", "wireless"]
weight: 5
---

# macOS AirPlay Not Working Fix

AirPlay errors include Apple TV not appearing, connections dropping mid-stream, audio-only when video expected, or "Unable to connect to AirPlay device."

## What This Error Means

AirPlay streams audio and video from Mac to Apple TV or AirPlay-enabled speakers over Wi-Fi. Failures indicate network issues, device compatibility problems, or AirPlay service failures.

## Common Causes

- Mac and Apple TV on different Wi-Fi networks
- Wi-Fi multicast or Bonjour disabled on router
- Apple TV firmware outdated
- Firewall blocking AirPlay ports
- AirPlay service crashed

## How to Fix

### 1. Check network connectivity

```bash
# Verify both devices are on the same network
networksetup -getairportnetwork en0

# Ping the Apple TV
ping <apple-tv-ip-address>
```

### 2. Restart AirPlay service

```bash
# Restart the AirPlay helper
killall AirPlayXPCHelper
```

### 3. Check firewall settings

```bash
# System Preferences > Security & Privacy > Firewall > Options
# Ensure "Block all incoming connections" is UNCHECKED
```

### 4. Reset AirPlay preferences

```bash
defaults delete com.apple.airplay
defaults delete com.apple.AirPlay
```

## Related Errors

- [Wi-Fi Error](macos-wifi-error) - Wi-Fi connectivity issues
- [Handoff Error](macos-handoff-error) - continuity feature issues
- [Bonjour Error](bonjour-error) - network service discovery
