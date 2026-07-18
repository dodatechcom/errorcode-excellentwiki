---
title: "[Solution] macOS WiFi Authentication Error — Incorrect Password or WPA Failure"
description: "Fix macOS WiFi authentication error: incorrect password, WiFi network requires credentials, WPA2/WPA3 auth failure."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 162
---

# WiFi Authentication Error — Incorrect Password or WPA Failure

Fix macOS WiFi authentication error: incorrect password, WiFi network requires credentials, WPA2/WPA3 auth failure.

## Common Causes

- WiFi password changed but Mac still using old credentials
- WPA3 authentication incompatible with older Mac hardware
- Corrupted WiFi password stored in macOS keychain
- Router security settings not compatible with macOS

## How to Fix

### 1. Forget and Rejoin WiFi Network

```bash
# System Settings → WiFi → Known Networks → Remove the network
# Rejoin with correct password
```

### 2. Delete WiFi Password from Keychain

```bash
security delete-generic-password -s 'AirPort' ~/Library/Keychains/login.keychain-db
# Rejoin WiFi network and enter password fresh
```

### 3. Check Router WPA Settings

```bash
# Router Settings → Wireless → Security → Use WPA2 Personal or WPA3
```

### 4. Reset Network Settings

```bash
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist
sudo shutdown -r now
```

## Common Scenarios

This error commonly occurs when:

- Mac keeps rejecting correct WiFi password
- WiFi authentication fails with 'incorrect password' even when password is right
- New WPA3 network not connecting to older Mac
- WiFi asks for password repeatedly but never connects

## Prevent It

- Update keychain password when WiFi network password changes
- Use WPA2 Personal for widest macOS device compatibility
- Forget and rejoin networks when authentication issues occur
- Keep macOS updated for latest WiFi security protocol support
