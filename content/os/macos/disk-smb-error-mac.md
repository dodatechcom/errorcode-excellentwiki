---
title: "[Solution] macOS Disk SMB Error — SMB Share Not Mounting"
description: "Fix macOS SMB connection error: SMB share not mounting, SMB server disconnects, slow SMB file transfers, SMB authentication fails."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 159
---

# Disk SMB Error — SMB Share Not Mounting

Fix macOS SMB connection error: SMB share not mounting, SMB server disconnects, slow SMB file transfers, SMB authentication fails.

## Common Causes

- SMB protocol version mismatch between Mac and server
- SMB share permissions not configured for Mac user
- Network latency causing SMB connection timeouts
- SMB cache corruption on Mac client side

## How to Fix

### 1. Check SMB Server Connection

```bash
ping SMB_SERVER_IP
smbutil status SMB_SERVER_IP
smbutil lookup SMB_SERVER_NAME
```

### 2. Mount SMB Share Manually

```bash
mount_smbfs //user:pass@SMB_SERVER_IP/ShareName /Volumes/SMBShare
```

### 3. Fix SMB Performance Issues

```bash
# System Settings → Network → Advanced → WINS → Set SMB version to 3
```

### 4. Clear SMB Cache

```bash
rm -rf ~/Library/Caches/com.apple.smbclient.*
rm -rf ~/Library/Preferences/com.apple.smbclient.*
sudo shutdown -r now
```

## Common Scenarios

This error commonly occurs when:

- SMB share asks for credentials repeatedly but never connects
- SMB file transfers are extremely slow compared to expected speed
- SMB share disconnects randomly during large file transfers
- SMB share appears in Finder but shows zero bytes of available space

## Prevent It

- Enable SMB 2 or SMB 3 on server for better macOS compatibility
- Clear SMB cache regularly if connection issues persist
- Keep server firmware updated to support latest SMB protocol versions
- Use wired Ethernet for SMB transfers requiring maximum speed
