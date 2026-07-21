---
title: "[Solution] macOS Installation Error 7 -- Installer Cannot Write to System Volume"
description: "Fix macOS installation error 7 when the installer is unable to write to the system volume. Resolve Mac OS install write failure."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Error 7 -- Installer Cannot Write to System Volume

Error code 7 means the installer cannot write files to the system volume. This is a write permission or disk space issue.

## Common Causes
- System volume is read-only (APFS sealed system volume behavior)
- Disk is full and cannot accept new files
- Disk is mounted read-only due to filesystem errors
- FileVault or third-party encryption is locking the volume
- Disk hardware failure preventing writes

## How to Fix
1. Check disk space -- you need at least 25 GB free
2. Boot into Recovery Mode and run First Aid on the startup volume
3. Check if the volume is mounted read-only and repair it
4. Disable FileVault if it is locking the system volume
5. Check disk hardware health using Apple Diagnostics

```bash
# Check if volume is mounted read-only
mount | grep disk1s1

# Verify disk space
df -h /
```

## Examples

```bash
# Run Apple Diagnostics
# Shut down, then hold D during startup on Intel Macs
# On Apple Silicon, hold power button and follow prompts
```

This error is common when the disk is nearly full, when filesystem corruption forces a read-only mount, or when FileVault is actively encrypting the volume.
