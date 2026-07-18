---
title: "[Solution] macOS App Store Download Error — Apps Stuck Downloading"
description: "Fix macOS App Store download failure: apps stuck on downloading, App Store download interrupted or spinning indefinitely."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 191
---

# App Store Download Error — Apps Stuck Downloading

Fix macOS App Store download failure: apps stuck on downloading, App Store download interrupted or spinning indefinitely.

## Common Causes

- App Store download cache corrupted
- Insufficient disk space for app download and installation
- Network interruption during app download
- Apple ID authentication token expired during download

## How to Fix

### 1. Clear App Store Download Cache

```bash
rm -rf ~/Library/Caches/com.apple.appstore
rm -rf ~/Library/Updates/*
killall 'App Store'
```

### 2. Check Disk Space

```bash
df -h /
# Ensure at least 2x app size free for download and installation
```

### 3. Reset Download and Try Again

```bash
# App Store → Account → find paused download → click Resume or Cancel and retry
```

### 4. Sign Out and Back Into Apple ID

```bash
# App Store → Store → Sign Out
# Wait 30 seconds → Sign In → Retry download
```

## Common Scenarios

This error commonly occurs when:

- App download stuck at 'Waiting...' or 'Loading...' indefinitely
- Download progress bar appears but never advances
- App Store shows download error with retry button that doesn't work
- Download starts but fails partway through with error

## Prevent It

- Ensure sufficient disk space before downloading large apps
- Keep stable internet connection during app downloads
- Clear App Store cache if downloads consistently fail
- Sign out and back into Apple ID if download authentication fails
