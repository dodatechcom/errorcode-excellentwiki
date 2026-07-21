---
title: "[Solution] macOS Install Stuck on Apple Logo -- Progress Bar Not Moving"
description: "Fix macOS installation stuck on Apple logo with progress bar frozen. Resolve Mac install hanging at Apple logo during update."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Stuck on Apple Logo -- Progress Bar Not Moving

When the macOS installer restarts the Mac, the Apple logo with a progress bar should advance. When the progress bar stalls, the installer may be processing in the background or may be stuck.

## Common Causes
- The installer is extracting files silently (progress may not update)
- APFS volume operations are slow on a nearly full disk
- FileVault is re-encrypting the volume during the install
- A kext is loading slowly or causing a delay
- The Mac hardware is too slow for the target macOS version

## How to Fix
1. Wait at least one hour -- some installations appear stuck but are progressing
2. Check if the Mac is warm or the SSD activity light is blinking
3. Boot into Safe Mode to skip non-essential processes and retry
4. Ensure the disk has at least 25 GB of free space
5. Use verbose boot (Command+V) to see what process is stalling

```bash
# Verbose boot to see where the install is stalling
# Hold Command+V during restart to see detailed boot messages
```

## Examples

```bash
# In Recovery Mode, check disk space
df -h /
```

This error is common on Macs with HDDs, when FileVault is enabled and the volume needs re-encryption, or when the Mac model is at the minimum specification for the target macOS version.
