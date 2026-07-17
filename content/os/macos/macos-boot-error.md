---
title: "[Solution] Mac Boot Error — Won't Start Up"
description: "Fix Mac boot errors when Mac won't start, shows black screen, blinking folder, or stuck at Apple logo during startup."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Mac Boot Error Fix

Boot errors prevent macOS from loading. The Mac may show a black screen, blinking folder with question mark, Apple logo with progress bar that stalls, or simply not power on.

## What This Error Means

The Mac boot sequence goes: firmware POST → EFI → bootloader → kernel → macOS. Boot errors can occur at any stage. The specific symptom indicates where the failure happens.

## Common Causes

- Corrupt system files preventing kernel load
- Boot disk not selected in startup preferences
- Corrupt APFS container or disk
- Third-party kernel extension blocking boot
- Hardware failure (SSD, RAM, logic board)

## How to Fix

### 1. Reset NVRAM and SMC

```bash
# NVRAM: Shut down → Turn on → Hold Option+Command+P+R for 20 sec
# SMC (Intel MacBook): Shut down → Hold Shift+Control+Option+Power for 10 sec
```

### 2. Boot in Safe Mode

```bash
# Intel: Hold Shift during startup
# Apple Silicon: Hold power button → select disk → hold Shift → Continue
# Safe Mode loads minimal extensions and runs disk checks
```

### 3. Use Disk Utility from Recovery

```bash
# Boot into Recovery (Cmd+R or Options)
# Run First Aid on the startup disk
# If disk is unrepairable, data recovery may be needed
```

### 4. Check startup disk selection

```bash
# Hold Option during startup to see bootable volumes
# Select your macOS startup disk
# Or set it in System Preferences → Startup Disk
```

## Related Errors

- [Firmware Error](macos-firmware-error) — firmware corruption
- [EFI Error](macos-efi-error) — EFI boot partition issues
- [Kernel Panic](kernel-panic) — kernel-level crashes
