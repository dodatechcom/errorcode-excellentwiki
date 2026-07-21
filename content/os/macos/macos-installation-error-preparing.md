---
title: "[Solution] macOS Installation Error Preparing -- Installer Stuck Preparing"
description: "Fix macOS installation stuck on preparing when the installer hangs during the preparation phase. Resolve Mac install stuck at preparing."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Error Preparing -- Installer Stuck Preparing

The installation preparation phase is when macOS extracts installer files, validates disk space, and creates APFS snapshots. When this phase stalls, the progress bar may show 'Preparing' for hours without advancing.

## Common Causes
- APFS snapshot creation failing due to disk errors
- Insufficient disk space for the preparation phase
- Corrupted installer package requiring re-download
- Spotlight indexing during the install consuming system resources
- Third-party disk encryption or security software interfering

## How to Fix
1. Wait at least 30 minutes -- some preparation phases are slow on older Macs
2. Check disk space -- preparation needs extra temporary space
3. Disable Spotlight temporarily before running the installer
4. Disconnect external drives that may be causing disk arbitration delays
5. Try running the installer from Safe Mode

```bash
# Disable Spotlight during install (re-enable after)
sudo mdutil -i off /
```

## Examples

```bash
# Monitor installer progress from terminal
log show --predicate 'process == "InstallAssistant"' --last 10m --style compact
```

This error is common on Macs with failing SSDs, when Spotlight is actively indexing a large library during the install, or when an external Thunderbolt dock is causing disk arbitration loops.
