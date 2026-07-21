---
title: "[Solution] macOS Installation Stuck Restarting -- Mac Reboots and Freezes"
description: "Fix macOS installation stuck on restarting when Mac freezes during the reboot phase. Resolve install restart loop on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Stuck Restarting -- Mac Reboots and Freezes

During macOS installation, the Mac restarts several times. When it gets stuck on a restart -- showing the Apple logo with no progress or cycling through restarts -- the installation is stuck.

## Common Causes
- Firmware update taking longer than expected (up to 30 minutes)
- APFS volume conversion or snapshot application stalling
- Corrupted system files being applied during the restart
- Power management issue causing premature sleep during install
- Incompatible startup item blocking the boot process

## How to Fix
1. Wait at least 30 minutes -- some restart phases are slow
2. Do not force shutdown during the firmware update phase
3. Ensure the Mac is plugged into power
4. If the restart loop continues, boot into Recovery Mode and run First Aid
5. As a last resort, erase and reinstall macOS

```bash
# Do NOT force shutdown during a firmware update
# This can permanently damage the firmware on Apple Silicon Macs
```

## Examples

```bash
# If you must recover, boot into DFU mode (Apple Silicon)
# and use Apple Configurator 2 on another Mac to restore
```

This error is most common during Apple Silicon firmware updates that take significantly longer than expected, after power loss during the install, or when a third-party startup item conflicts with the new system.
