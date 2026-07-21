---
title: "[Solution] macOS Update Failed to Install -- Update Error on Mac"
description: "Fix macOS update failed to install when the download completes but installation fails. Resolve Mac update error during install phase."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Update Failed to Install -- Update Error on Mac

After a macOS update successfully downloads, the installation phase may fail with an error message like 'macOS could not be installed on your computer' or the Mac restarts and rolls back the update.

## Common Causes
- Insufficient free disk space on the startup volume
- Corrupted download that passed verification but has bad files
- Third-party kexts incompatible with the new macOS version
- FileVault encryption locking files during the update
- Incorrect date and time settings preventing certificate validation

## How to Fix
1. Free up at least 25 GB of space on the startup volume
2. Delete cached update files and re-download
3. Boot into Safe Mode to disable third-party extensions, then retry
4. Check date and time in System Preferences -- set to automatic
5. Use the full installer from App Store for a more reliable installation

```bash
# Check disk space
df -h /

# Clear update cache and retry
sudo rm -rf /Library/Updates/*
softwareupdate --fetch-full-installer --full-installer-version 14.5
```

## Examples

```bash
# Check system date (must be correct for Apple certificates)
date

# Force automatic date/time
sudo sntp -sS time.apple.com
```

This error commonly occurs when the startup volume has less than 25 GB free, when a third-party antivirus locks system files during the update, or when the system clock is incorrect.
