---
title: "[Solution] macOS Installation Error 4 -- Installer Package Damaged"
description: "Fix macOS installation error 4 when the installer package is reported as damaged. Resolve Mac OS install package damage error."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Error 4 -- Installer Package Damaged

Error code 4 indicates the installer package is damaged beyond what a simple re-download can fix. The internal structure of the installer has been corrupted.

## Common Causes
- APFS volume corruption affecting stored files
- Installer was copied to the disk with errors
- Sudden shutdown corrupted the installer file
- Disk full during download caused a truncated file
- Third-party file system utilities modifying the installer

## How to Fix
1. Verify disk health using Disk Utility First Aid
2. Clear the Software Update cache and delete the installer
3. Re-download the installer after repairing disk errors
4. If the disk has persistent errors, back up data and reformat
5. Try downloading the installer on a different Mac and copying via USB

```bash
# Repair disk from Recovery Mode
# Boot with Command+R, open Disk Utility, run First Aid

# Clear update cache
sudo rm -rf /Library/Updates/*
sudo rm -rf /Applications/Install\ macOS\*.app
```

## Examples

```bash
# Check disk health
diskutil verifyVolume disk1s1
```

This error commonly occurs after a forced shutdown, when the disk has bad sectors, or when the startup volume has filesystem corruption that needs repair.
