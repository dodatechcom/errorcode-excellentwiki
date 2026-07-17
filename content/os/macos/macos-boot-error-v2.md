---
title: "[Solution] Mac Boot Error - Folder with Question Mark"
description: "Fix Mac boot errors when startup shows a folder with question mark, flashing folder, or cannot find startup disk."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Mac Boot Error - Folder with Question Mark

Mac displays a folder with a question mark at startup, flashing folder icon, or "No bootable device" error.

## What This Error Means

The folder with question mark means macOS cannot find a valid startup disk. This occurs when the startup disk is corrupted, the boot loader is missing, or the disk is not properly connected.

## Common Causes

- Startup disk corruption
- Missing or corrupted boot loader
- Disk not properly connected (loose cable)
- Failed disk encryption recovery
- APFS container corruption
- Disk partition table damage

## How to Fix

### Try Recovery Mode

```bash
# Intel Mac: Restart holding Cmd+R
# Apple Silicon: Hold power button, select Recovery

# In Recovery, open Disk Utility
# Run First Aid on startup disk
```

### Check Startup Disk

```bash
# In Recovery Mode, open Terminal

# List all disks
diskutil list

# Check startup disk
diskutil info disk0

# Try to mount startup disk
diskutil mount disk0s1
```

### Repair Disk

```bash
# Boot into Recovery Mode

# Open Disk Utility
# Select startup disk
# Click "First Aid"

# Or from Recovery Terminal:
diskutil verifyVolume disk0s1
diskutil repairVolume disk0s1
```

### Reset NVRAM

```bash
# Intel Mac: Restart holding Option+Cmd+P+R for 20 seconds
# Apple Silicon: NVRAM reset automatic

# Reset startup disk
nvram -c
```

### Reinstall macOS

```bash
# Boot into Recovery Mode
# Select "Reinstall macOS"
# Follow installation wizard
# This preserves data if possible
```

### Check Hardware

```bash
# Run Apple Diagnostics
# Intel: Restart holding D key
# Apple Silicon: Hold power button, select Diagnostics

# Check for hardware issues:
# - Disk cable connection
# - Disk failure
# - Logic board issues
```

### Force Startup Disk Selection

```bash
# Hold Option key during restart
# Select startup disk from boot menu

# Or in Recovery:
# Open Startup Disk utility
# Select your macOS volume
```

## Related Errors

- [Firmware Update Error]({{< relref "/os/macos/macos-firmware-update-error" >}}) — Firmware issues
- [SSD Error]({{< relref "/os/macos/macos-ssd-error-v2" >}}) — Storage issues
- [macOS Recovery Error]({{< relref "/os/macos/macos-macos-recovery-error" >}}) — Recovery mode
