---
title: "[Solution] macOS Blue Screen of Death (BSOD)"
description: "Fix macOS blue screen of death. Resolve blue screen crashes caused by display driver issues, corrupt system files, and hardware failures."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["blue-screen", "bsod", "crash", "display", "boot"]
weight: 5
---

# macOS Blue Screen of Death Fix

A blue screen on macOS indicates a critical system error that prevents the OS from continuing. Unlike Windows BSOD, macOS typically shows a blue screen briefly before restarting or kernel panicking.

## What This Error Means

The blue screen appears when macOS encounters a fatal error during boot or normal operation. It may display a progress bar that never completes, or flash blue before the system restarts. This is often a precursor to a kernel panic.

## Common Causes

- Corrupt system files after a failed macOS update
- Incompatible kernel extensions (kexts)
- Faulty display hardware or GPU
- Corrupt NVRAM settings
- File system corruption on the boot volume

## How to Fix

### 1. Boot into Safe Mode

```bash
# Intel Mac: Hold Shift during startup
# Apple Silicon: Hold power button → select disk → hold Shift → Continue
# Safe mode loads only essential kexts and runs disk checks
```

### 2. Boot into Recovery Mode and run Disk First Aid

```bash
# Intel: Hold Cmd+R during startup
# Apple Silicon: Hold power button → Options → Continue
# Open Disk Utility → Select startup disk → First Aid
```

### 3. Reset NVRAM/PRAM

```bash
# Shut down Mac
# Turn on and immediately hold Option+Command+P+R for 20 seconds
# Release and let Mac boot normally
```

### 4. Reinstall macOS without erasing data

```bash
# Boot into Recovery Mode (Cmd+R or Options)
# Select "Reinstall macOS"
# This replaces system files while keeping your data intact
```

### 5. Check system logs before the crash

```bash
# If you can boot to terminal (Recovery or Single User Mode)
log show --predicate 'eventMessage contains "blue screen"' --last 1h

# Check for crash reports
ls -lt /Library/Logs/DiagnosticReports/ | head -20
```

## Related Errors

- [Kernel Panic](kernel-panic) — general kernel panic and restart errors
- [Disk Utility Error](disk-utility-error) — file system corruption issues
- [GPU Kernel Panic](macos-kernel-panic-gpu) — GPU-related crashes
