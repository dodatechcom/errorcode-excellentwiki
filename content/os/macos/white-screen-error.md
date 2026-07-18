---
title: "[Solution] macOS White Screen Error — Stuck on White Screen at Boot"
description: "Fix macOS white screen: display stuck on white screen during boot, system does not progress to Apple logo or login window."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 107
---

# White Screen Error — Stuck on White Screen at Boot

Fix macOS white screen: display stuck on white screen during boot, system does not progress to Apple logo or login window.

## Common Causes

- GPU failing to initialize display output during early boot
- Corrupted PRAM/NVRAM preventing normal boot sequence
- Startup disk not being recognized by firmware
- Hardware failure in display or logic board

## How to Fix

### 1. Reset NVRAM Immediately

```bash
# Hold power button 10s to shut down
Hold Option+Command+P+R for 20 seconds
```

### 2. Boot from Recovery or External Drive

```bash
# Intel: Hold Command+R during startup
diskutil list
```

### 3. Check and Repair Startup Disk

```bash
diskutil verifyVolume disk0s1
# From Recovery Terminal
```

### 4. Test with Safe Mode Boot

```bash
# Intel: Hold Shift during startup
kextstat | grep -v com.apple
```

## Common Scenarios

This error commonly occurs when:

- White screen appears immediately after power button is pressed
- White screen occurred after SMC reset or NVRAM corruption
- System shows white screen but external display shows normal boot
- White screen happens intermittently but Mac eventually boots normally

## Prevent It

- Reset NVRAM at first sign of white screen during boot
- Keep macOS updated to ensure firmware compatibility
- Avoid forcing shutdowns which can corrupt NVRAM settings
- Have Apple Diagnostics ready to run if white screen persists
