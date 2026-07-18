---
title: "[Solution] macOS Disk Network Drive Error — NAS Share Not Mounting"
description: "Fix macOS network drive error: NAS or network share not mounting, SMB/AFP connection fails for shared disks on network storage."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 153
---

# Disk Network Drive Error — NAS Share Not Mounting

Fix macOS network drive error: NAS or network share not mounting, SMB/AFP connection fails for shared disks on network storage.

## Common Causes

- Network connectivity issue between Mac and NAS device
- SMB/AFP protocol version mismatch
- NAS device firmware incompatibility with macOS
- DNS resolution failure for network drive hostname

## How to Fix

### 1. Check Network Connectivity to NAS

```bash
ping NAS_IP_ADDRESS
nslookup NAS_hostname
smbutil status NAS_IP_ADDRESS
```

### 2. Mount Network Drive Manually

```bash
mount_smbfs //user:pass@NAS_IP/sharename /Volumes/ShareName
mount_afp afp://user@NAS_IP/sharename /Volumes/ShareName
```

### 3. Check SMB/AFP Protocol Settings

```bash
# NAS Settings → Enable SMB 2/3 and AFP protocols
```

### 4. Fix DNS Resolution

```bash
nslookup NAS_hostname
# Add NAS hostname to /etc/hosts if DNS fails
```

## Common Scenarios

This error commonly occurs when:

- Network drive not appearing in Finder sidebar
- NAS share asks for credentials repeatedly but never connects
- SMB share mounts but files are inaccessible or read-only
- Network drive disconnects after Mac wakes from sleep

## Prevent It

- Enable SMB 2 or SMB 3 on NAS device for macOS compatibility
- Keep NAS firmware updated for macOS network sharing support
- Add NAS hostname to /etc/hosts for reliable DNS resolution
- Map network drive as login item for automatic mounting at startup
