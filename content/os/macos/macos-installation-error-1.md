---
title: "[Solution] macOS Installation Error 1 -- Installer Failed With Exit Code 1"
description: "Fix macOS installation error 1 when the installer exits with code 1. Resolve Mac OS install failure with exit status 1."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Error 1 -- Installer Failed With Exit Code 1

Exit code 1 from the macOS installer indicates a general failure. The installer encountered an error that prevented it from completing but does not provide a specific diagnostic code.

## Common Causes
- Disk full or not enough space for the installation files
- Permission denied when writing to the system volume
- Corrupted disk image or installer package
- Kernel extension blocking the installer process
- APFS container errors preventing volume operations

## How to Fix
1. Check disk space using Disk Utility or terminal
2. Boot into Recovery Mode and run First Aid on the startup volume
3. Clear the installer cache and re-download
4. Boot into Safe Mode and attempt installation
5. Use a fresh USB installer created on a different Mac

```bash
# Check disk space
df -h /

# Run First Aid from Recovery Mode
# Boot with Command+R, open Disk Utility, select startup disk, click First Aid
```

## Examples

```bash
# Check for disk errors from Recovery terminal
diskutil verifyVolume disk1s1
diskutil repairVolume disk1s1
```

This error is common when the startup disk has errors that Disk Utility can repair, when third-party kexts are blocking the installer, or when the installer file is corrupted.
