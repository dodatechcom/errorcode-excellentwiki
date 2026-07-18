---
title: "[Solution] macOS Target Disk Mode Error — Mac Not Appearing as External Disk"
description: "Fix macOS Target Disk Mode failure: Mac not appearing as external disk when connected via Thunderbolt or USB-C for file transfer."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 148
---

# Target Disk Mode Error — Mac Not Appearing as External Disk

Fix macOS Target Disk Mode failure: Mac not appearing as external disk when connected via Thunderbolt or USB-C for file transfer.

## Common Causes

- Target Disk Mode not supported on Apple Silicon Macs
- Thunderbolt or USB-C cable not supporting Target Disk Mode
- Mac firmware issue preventing Target Disk Mode activation
- FileVault encryption blocking Target Disk Mode access

## How to Fix

### 1. Try Target Disk Mode Startup

```bash
# Intel: Shut down → Hold T key while pressing power button
# Apple Silicon: Use Share Disk instead of Target Disk Mode
```

### 2. Use Share Disk on Apple Silicon

```bash
# Both Macs sign into same Apple ID
# Apple menu → System Settings → General → Sharing → Share Disk
```

### 3. Check Thunderbolt Connection

```bash
system_profiler SPThunderboltDataType
# Use Thunderbolt 3/4 cable, not USB-C only cable
```

### 4. Disable FileVault for Target Disk Mode

```bash
# System Settings → Privacy & Security → FileVault → Turn Off temporarily
```

## Common Scenarios

This error commonly occurs when:

- Mac does not appear as external disk when T key is held during boot
- Target Disk Mode works intermittently or disconnects frequently
- Connected Mac shows in Thunderbolt devices but not as disk
- Apple Silicon Mac does not respond to T key at startup

## Prevent It

- Use Share Disk on Apple Silicon Macs instead of Target Disk Mode
- Ensure Thunderbolt cable supports data transfer, not just charging
- Disable FileVault temporarily when using Target Disk Mode
- Keep both Macs updated for Target Disk Mode compatibility
