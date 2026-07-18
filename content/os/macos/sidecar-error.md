---
title: "[Solution] macOS Sidecar Error — iPad Cannot Be Used as Second Display"
description: "Fix macOS Sidecar not working: cannot use iPad as second display or drawing tablet with Mac, Sidecar connection fails."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 124
---

# Sidecar Error — iPad Cannot Be Used as Second Display

Fix macOS Sidecar not working: cannot use iPad as second display or drawing tablet with Mac, Sidecar connection fails.

## Common Causes

- iPad and Mac not signed into same Apple ID with iCloud
- Bluetooth or Wi-Fi disabled preventing Sidecar discovery
- iPad or Mac software too old for current Sidecar version
- Apple Pencil not supported with current Mac or iPad combination

## How to Fix

### 1. Verify Sidecar Compatibility

```bash
system_profiler SPHardwareDataType | grep 'Model Name'
sw_vers
# Sidecar requires macOS Catalina+ and iPadOS 13+
```

### 2. Connect iPad via Sidecar

```bash
# System Settings → Displays → Add Display → Select iPad
```

### 3. Fix Sidecar Connection Drops

```bash
ping $(ipconfig getifaddr en0)
# iPad Settings → General → Transfer or Reset iPad → Reset Network Settings
```

### 4. Configure Sidecar Display Settings

```bash
# System Settings → Displays → Select iPad → Arrange display position
```

## Common Scenarios

This error commonly occurs when:

- Sidecar does not detect iPad even though both are on same Apple ID
- Sidecar connects but display is black or not responding
- Apple Pencil input not working in Sidecar on iPad
- Sidecar connection drops frequently when using wirelessly

## Prevent It

- Keep both Mac and iPad updated to latest macOS and iPadOS versions
- Use wired connection for more reliable Sidecar performance
- Ensure strong Wi-Fi signal between Mac and iPad for wireless Sidecar
- Restart both devices if Sidecar connection becomes unstable
