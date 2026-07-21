---
title: "[Solution] macOS Installation Extremely Slow -- Install Taking Too Long"
description: "Fix macOS installation taking extremely long when install progress is very slow. Resolve Mac OS install speed issues."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Extremely Slow -- Install Taking Too Long

A slow macOS installation can take anywhere from 30 minutes to several hours depending on the Mac model, storage type, and network speed.

## Common Causes
- Slow HDD instead of SSD as the startup disk
- Large amount of data being migrated during install
- Network-based installation downloading components during install
- Spotlight or other processes competing for disk I/O
- APFS container running low on free space

## How to Fix
1. Check if your startup disk is an HDD or SSD
2. Disconnect from the internet to prevent background downloads during install
3. Ensure at least 30 GB of free space on the startup volume
4. Close all applications before starting the installation
5. Consider upgrading to an SSD if the Mac uses a mechanical hard drive

```bash
# Check storage type
system_profiler SPStorageDataType | grep -i "medium_type\|physical_drive"
```

## Examples

```bash
# Monitor installation progress from terminal
log show --predicate 'process == "InstallAssistant"' --last 5m --style compact
```

This error is common on older Macs with HDDs, when migrating large user folders during the install, or when the installer is downloading additional components over a slow connection.
