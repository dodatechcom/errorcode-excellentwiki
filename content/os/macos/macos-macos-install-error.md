---
title: "[Solution] macOS Installation Error"
description: "Fix macOS installation errors when upgrading or fresh installing macOS. Resolve 'Installation failed,' 'needs more disk space,' and other install errors."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS Installation Error Fix

macOS installation errors occur during OS upgrades or fresh installs. Common messages include "Installation failed," "This copy of macOS is damaged," or "needs more disk space."

## What This Error Means

The macOS installer validates system requirements, verifies the installer integrity, and applies the update. Failures can indicate damaged installer files, incompatible hardware, or disk issues.

## Common Causes

- Damaged or incomplete macOS installer download
- Insufficient disk space (typically 20+ GB needed)
- Corrupt Recovery partition
- Third-party security software blocking installation
- Hardware incompatibility
- Incorrect date/time settings

## How to Fix

### 1. Re-download the installer

```bash
# Delete the existing installer
rm -rf /Applications/Install\ macOS*.app

# Re-download from App Store or Apple's support page
softwareupdate --fetch-full-installer --full-installer-version 14.2
```

### 2. Verify installer integrity

```bash
# Check installer checksum
shasum -a 256 /Applications/Install\ macOS*.app/Contents/SharedSupport/InstallESD.dmg

# Compare with Apple's published checksum
```

### 3. Boot into Recovery and install

```bash
# Intel: Hold Cmd+R during startup
# Apple Silicon: Hold power button → Options → Continue
# Select "Reinstall macOS" from macOS Utilities
```

### 4. Check disk health before installing

```bash
# Verify disk
diskutil verifyVolume /

# Repair if needed (from Recovery)
diskutil repairVolume /
```

## Related Errors

- [macOS Recovery Error](macos-macos-recovery) — recovery mode issues
- [Software Update Error](macos-macos-update-error) — incremental update failures
- [Disk Utility Error](disk-utility-error) — disk repair errors
