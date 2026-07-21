---
title: "[Solution] macOS Installation Boot Error -- Mac Cannot Boot After Install"
description: "Fix macOS boot error after installation when Mac fails to start after updating. Resolve boot failure after Mac OS install."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Boot Error -- Mac Cannot Boot After Installation

After the macOS installation completes and the Mac restarts, the system may fail to boot. This can manifest as a black screen, flashing folder, prohibitory symbol, or an endless restart loop.

## Common Causes
- Boot volume was not correctly set after the installation
- APFS snapshot commit failed during the final restart
- Firmware update was not applied before the reboot
- Third-party kexts are incompatible with the new macOS version
- Bootloader corruption on multi-boot Macs

## How to Fix
1. Reset NVRAM and try booting again
2. Boot into Safe Mode to bypass incompatible kexts
3. Use Recovery Mode to check the boot volume with Disk Utility
4. Verify the startup disk is correctly set via Recovery Mode Startup Disk
5. On Apple Silicon, hold the power button to access startup options

```bash
# From Recovery Mode terminal
diskutil list
diskutil apfs listVolumes
```

## Examples

```bash
# Check the bless record for the startup disk
bless --info --verbose /
bless --info --verbose --getboot
```

This error is common on multi-boot Macs with Boot Camp, when incompatible kexts are loaded from a previous installation, or when the APFS snapshot commit failed due to a power interruption.
