---
title: "[Solution] macOS WiFi VPN Error — VPN Disconnects on WiFi"
description: "Fix macOS WiFi VPN error: VPN disconnects on WiFi, VPN slow over WiFi, VPN cannot establish tunnel, VPN conflicts with WiFi."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 165
---

# WiFi VPN Error — VPN Disconnects on WiFi

Fix macOS WiFi VPN error: VPN disconnects on WiFi, VPN slow over WiFi, VPN cannot establish tunnel, VPN conflicts with WiFi.

## Common Causes

- WiFi sleep/power management disconnecting VPN tunnel
- VPN protocol incompatible with WiFi network settings
- DNS leak preventing VPN from routing all traffic
- VPN configuration conflict with WiFi proxy settings

## How to Fix

### 1. Check VPN and WiFi Status

```bash
scutil --dns | grep '# -- DNS --'
# Check VPN connection status in System Settings → Network
```

### 2. Disable WiFi Power Management

```bash
sudo pmset -a womp 0
sudo pmset -a powernap 0
# System Settings → Network → WiFi → Details → Power Nap → Off
```

### 3. Fix DNS Leak in VPN

```bash
# System Settings → Network → VPN → Details → DNS → Ensure VPN DNS is primary
```

### 4. Reset VPN Configuration

```bash
# System Settings → Network → VPN → Remove and re-add VPN connection
# Restart Mac and reconnect VPN
```

## Common Scenarios

This error commonly occurs when:

- VPN disconnects every time Mac wakes from sleep
- VPN connection is extremely slow when on WiFi
- VPN cannot establish tunnel when connected to certain WiFi networks
- VPN works on Ethernet but fails on WiFi

## Prevent It

- Configure VPN to reconnect automatically after WiFi disconnects
- Disable WiFi power management features that interrupt VPN tunnels
- Use wired Ethernet for VPN when maximum stability is required
- Keep VPN client updated for latest WiFi protocol compatibility
