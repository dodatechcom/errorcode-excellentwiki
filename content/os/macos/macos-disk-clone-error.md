---
title: "[Solution] macOS Disk Clone Error -- Disk Cloning Failed on Mac"
description: "Fix macOS disk clone error when disk cloning or duplication fails. Resolve cloning errors on Mac using Disk Utility or terminal."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Disk Clone Error -- Disk Cloning Failed on Mac

Disk cloning creates an exact copy of one disk to another. When cloning fails, it may be due to disk errors, insufficient space, or format incompatibilities.

## Common Causes
- Source disk has errors that halt the cloning process
- Destination disk is smaller than the source
- Destination disk format is incompatible
- Disk is in use during the cloning process
- Bad sectors on either disk interrupt the copy

## How to Fix
1. Run First Aid on both source and destination disks
2. Ensure the destination disk is larger than or equal to the source
3. Boot from Recovery Mode or an external drive to clone
4. Use Disk Utility's Restore function for reliable cloning
5. Use terminal dd or asr for more control

```bash
# Clone using Disk Utility Restore
# Open Disk Utility > Select destination disk > Click Restore > Select source

# Clone using asr from terminal
sudo asr --source /dev/disk1 --target /dev/disk2 --erase
```

## Examples

```bash
# Check disk sizes to ensure destination is large enough
diskutil list
```

This error is common when the destination disk is too small, when the source disk has bad sectors, or when the cloning is interrupted by a system sleep or disconnect.
