---
title: "[Solution] Mac Firmware Update Error"
description: "Fix Mac firmware update errors on macOS. Resolve firmware update failures, stuck updates, and firmware verification errors on Apple Silicon and Intel Macs."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Mac Firmware Update Error

Firmware update errors occur when the Mac's firmware (BridgeOS on Apple Silicon, EFI on Intel) fails to update. This may manifest as a stuck Apple logo progress bar, firmware verification failure, or bricked device during update.

## What This Error Means

Apple Silicon Macs have two processor systems: the main SoC (running macOS) and the BridgeOS coprocessor (handling secure boot, Touch ID, etc.). Both need separate firmware updates. Firmware updates happen during macOS updates but can fail if power is interrupted, the image is corrupted, or hardware is faulty.

## Common Causes

- Power interruption during firmware update (most common)
- Corrupt macOS installer image
- Hardware issue (disk, memory)
- Network issue during OTA update download
- Third-party security software blocking firmware verification
- Firmware version incompatible with current macOS

## How to Fix

### Ensure Stable Power Connection

For laptops, keep the Mac plugged in and charging throughout the entire update process. For desktops, ensure the UPS or power supply is stable.

### Check Current Firmware Version

```bash
# Apple Silicon
system_profiler SPHardwareDataType

# Intel
system_profiler SPHardwareDataType | grep "Boot ROM"
```

### Use Full Installer (Not OTA)

```bash
# Download full macOS installer
softwareupdate --fetch-full-installer --full-installer-version 14.0

# Create bootable USB
sudo /Applications/Install\ macOS\ Sonoma.app/Contents/Resources/createinstallmedia --volume /Volumes/USB
```

### Reset SMC/NVRAM

```bash
# Intel: Reset SMC
# Shut down, unplug power for 30 seconds, plug in, turn on

# Intel: Reset NVRAM
# Hold Option+Command+P+R for 20 seconds during startup
```

### Use Apple Diagnostics

```bash
# Intel: Hold D during startup
# Apple Silicon: Hold power button, then Command+D
```

### DFU Recovery (Apple Silicon)

If firmware update bricked the Mac:

1. Connect to another Mac via USB-C.
2. On the host Mac, open Apple Configurator 2.
3. Put the bricked Mac into DFU mode:
   - Power off
   - Press and hold power button
   - Press and hold right Shift + left Control + left Option for 10 seconds
   - Release all three keys but keep holding power button
4. In Apple Configurator 2, right-click the Mac > **Restore**.

### Contact Apple Support

If firmware update fails repeatedly, it may indicate a hardware issue requiring Apple service.

## Related Errors

- [macOS Update Error]({{< relref "/os/macos/macos-macos-update-error-v2" >}}) — macOS software update issues
- [Kernel Panic]({{< relref "/os/macos/kernel-panic" >}}) — Kernel panic errors
- [macOS Recovery]({{< relref "/os/macos/macos-macos-recovery" >}}) — macOS Recovery mode
