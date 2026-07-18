---
title: "[Solution] macOS WiFi Airport Error — AirPort Utility Cannot Find Device"
description: "Fix macOS Airport utility error: Airport base station not detected, Airport utility cannot configure device, AirPort Extreme not responding."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 168
---

# WiFi Airport Error — AirPort Utility Cannot Find Device

Fix macOS Airport utility error: Airport base station not detected, Airport utility cannot configure device, AirPort Extreme not responding.

## Common Causes

- AirPort base station firmware outdated or unsupported
- Bonjour service failure preventing AirPort device discovery
- Network configuration preventing AirPort discovery
- AirPort hardware failure requiring service or replacement

## How to Fix

### 1. Check AirPort Device Discovery

```bash
dns-sd -B _airport._tcp local.
ping AIRPORT_IP_ADDRESS
open -a 'AirPort Utility'
```

### 2. Update AirPort Firmware

```bash
open -a 'AirPort Utility'
# Select AirPort device → Check for firmware updates
```

### 3. Reset AirPort Device

```bash
# Press and hold reset button on AirPort for 10 seconds
# Device will restart with factory defaults
```

### 4. Connect AirPort via Ethernet

```bash
# Connect Mac directly to AirPort with Ethernet cable for initial setup
```

## Common Scenarios

This error commonly occurs when:

- AirPort Utility shows 'No AirPort devices found'
- AirPort Extreme status light is amber instead of green
- Cannot configure AirPort base station through AirPort Utility
- AirPort device intermittently disappears from network

## Prevent It

- Keep AirPort firmware updated through AirPort Utility
- Place AirPort base station centrally for best WiFi coverage
- Reset AirPort device if it becomes unresponsive
- Consider alternative WiFi solutions as AirPort is discontinued
