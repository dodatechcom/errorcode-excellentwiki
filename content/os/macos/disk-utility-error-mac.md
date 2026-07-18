---
title: "[Solution] macOS Disk Utility Error — Disk Utility App Not Working"
description: "Fix macOS Disk Utility not working: Disk Utility app fails to open, cannot repair or format disks, First Aid option grayed out."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 131
---

# Disk Utility Error — Disk Utility App Not Working

Fix macOS Disk Utility not working: Disk Utility app fails to open, cannot repair or format disks, First Aid option grayed out.

## Common Causes

- Disk Utility preferences corrupted preventing app from launching
- System Integrity Protection blocking Disk Utility operations
- Corrupted Disk Utility application bundle or system files
- Insufficient permissions to perform disk operations

## How to Fix

### 1. Open Disk Utility from Recovery Mode

```bash
# Intel: Restart and hold Command+R
# Apple Silicon: Hold power button → Options → Recovery
# Open Disk Utility from Recovery Utilities menu
```

### 2. Reset Disk Utility Preferences

```bash
rm -f ~/Library/Preferences/com.apple.DiskUtility.plist
sudo rm -rf /Library/Caches/com.apple.preference*
sudo shutdown -r now
```

### 3. Reinstall Disk Utility via Recovery

```bash
# Recovery → Reinstall macOS to restore Disk Utility
```

### 4. Check System Integrity Protection

```bash
csrutil status
```

## Common Scenarios

This error commonly occurs when:

- Disk Utility app icon bounces in Dock but never opens
- First Aid button is grayed out when trying to repair disk
- Disk Utility shows 'Could not mount disk' for all connected drives
- Disk Utility window appears blank without any disk information

## Prevent It

- Keep macOS updated to receive Disk Utility improvements
- Run Disk Utility from Recovery mode if normal mode fails
- Avoid third-party disk management tools that may conflict
- Back up data before performing disk repair operations
