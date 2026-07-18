---
title: "[Solution] macOS MDS Error — Metadata Server Failure"
description: "Fix macOS metadata server (mds) error: mds_stores high CPU usage, Spotlight indexing fails, search functionality completely broken."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 112
---

# MDS Error — Metadata Server Failure

Fix macOS metadata server (mds) error: mds_stores high CPU usage, Spotlight indexing fails, search functionality completely broken.

## Common Causes

- Corrupted metadata store files requiring rebuild
- mds_stores process consuming excessive CPU during indexing
- Low disk space preventing mds from writing metadata
- Permission issue preventing mds from accessing indexed folders

## How to Fix

### 1. Check mds Process Status

```bash
ps aux | grep -i mds
top -l 1 -o mem -n 5 | grep mds
log show --predicate 'process == "mds"' --last 1h | grep -i error | head -20
```

### 2. Stop and Restart mds Daemon

```bash
sudo killall mds
sudo killall mds_stores
```

### 3. Rebuild Metadata Store

```bash
sudo mdutil -E /
sudo mdutil -E -a
sudo rm -rf /.Spotlight-V100
sudo mdutil -i on /
```

### 4. Check Disk Space and Permissions

```bash
df -h /
sudo rm -rf /Library/Caches/*
diskutil verifyVolume disk0s1
```

## Common Scenarios

This error commonly occurs when:

- mds_stores consumes all available CPU and system becomes unresponsive
- Spotlight search returns no results after macOS update
- mds process appears in Activity Monitor using excessive memory
- System log shows repeated mds crash and restart entries

## Prevent It

- Maintain at least 15% free disk space for metadata operations
- Restart Mac weekly to prevent mds memory leaks from accumulating
- Avoid changing permissions on system folders that mds needs to index
- Update macOS to receive mds performance improvements
