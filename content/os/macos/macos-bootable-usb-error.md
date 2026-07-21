---
title: "[Solution] macOS Bootable USB Error -- Cannot Create or Boot From USB Installer"
description: "Fix macOS bootable USB error when creating or booting from a USB installer fails. Resolve bootable USB issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Bootable USB Error -- Cannot Create or Boot From USB Installer

A bootable USB installer allows you to install or reinstall macOS when Recovery Mode is unavailable. When creation or booting fails, you cannot use the USB installer.

## Common Causes
- USB drive is not formatted correctly (must be Mac OS Extended)
- createinstallmedia command failed or was interrupted
- USB drive is too small (minimum 12 GB required)
- Firmware password prevents booting from external media
- USB drive is corrupted or failing

## How to Fix
1. Format the USB drive as Mac OS Extended (Journaled) with GUID partition map
2. Re-run the createinstallmedia command
3. Use a USB drive with at least 12 GB of space
4. Disable firmware password temporarily if set
5. Try a different USB drive

```bash
# Format USB drive
diskutil eraseDisk Journaled "USB" GPT /dev/disk2

# Create bootable USB installer
sudo /Applications/Install\ macOS\ Sequoia.app/Contents/Resources/createinstallmedia --volume /Volumes/USB
```

## Examples

```bash
# Verify the USB installer was created correctly
diskutil list /dev/disk2
```

This error is common when the USB drive is not formatted correctly, when the createinstallmedia command is interrupted, or when a firmware password prevents booting from external media.
