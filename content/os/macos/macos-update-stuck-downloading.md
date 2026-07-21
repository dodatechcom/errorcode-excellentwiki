---
title: "[Solution] macOS Update Stuck Downloading -- Software Update Freezes"
description: "Fix macOS update stuck on downloading when Software Update freezes. Resolve Mac update not progressing past downloading."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Update Stuck Downloading -- Software Update Freezes

When macOS Software Update appears to freeze during the download phase, the progress bar may stall for hours. The update file is either not downloading, is corrupted, or the connection to Apple servers has stalled.

## Common Causes
- Unstable internet connection dropping the download repeatedly
- Apple CDN server throttling or regional outage
- Cached update files in /Library/Updates are corrupted
- VPN or proxy interfering with the download
- Insufficient disk space for the temporary download files

## How to Fix
1. Cancel the current update attempt and restart your Mac
2. Clear the Software Update cache from terminal
3. Check available disk space -- you need at least 15-25 GB free
4. Disable any VPN or proxy before retrying the download
5. Use terminal to trigger the update download directly

```bash
# Clear the Software Update cache
sudo rm -rf /Library/Updates/*
sudo softwareupdate --clear-catalog

# Check for available updates from terminal
softwareupdate -l

# Download an update directly
softwareupdate --fetch-full-installer --full-installer-version 14.5
```

## Examples

```bash
# Monitor the download progress
softwareupdate --list 2>&1 | grep -i "Title\|Version\|Size"
```

This error commonly occurs during peak update periods when Apple servers are congested, on networks with strict bandwidth limits, or when a previous incomplete download is corrupting the update cache.
