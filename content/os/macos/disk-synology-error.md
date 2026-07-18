---
title: "[Solution] macOS Disk Synology Error — Synology NAS Not Accessible"
description: "Fix macOS Synology NAS error: Synology shared folder not mounting, DSM not accessible from Mac, Synology Finder integration fails."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 155
---

# Disk Synology Error — Synology NAS Not Accessible

Fix macOS Synology NAS error: Synology shared folder not mounting, DSM not accessible from Mac, Synology Finder integration fails.

## Common Causes

- Synology DSM not configured for SMB/AFP sharing
- Mac and Synology on different network subnets
- Synology firewall blocking Mac connection
- SMB protocol version incompatibility

## How to Fix

### 1. Check Synology DSM Connection

```bash
ping SYNOLOGY_IP
open http://SYNOLOGY_IP:5000
# Login to DSM and check shared folder settings
```

### 2. Mount Synology Share

```bash
mount_smbfs //admin:pass@SYNOLOGY_IP/SharedFolder /Volumes/SharedFolder
# Or use Finder → Go → Connect to Server
```

### 3. Enable SMB on Synology DSM

```bash
# Control Panel → File Services → Enable SMB/AFP/NFS → Apply
```

### 4. Fix Finder Integration

```bash
# System Settings → Network → Advanced → WINS → Set Workgroup to same as Synology
```

## Common Scenarios

This error commonly occurs when:

- Synology shared folder not appearing in Finder
- Cannot connect to Synology DSM web interface from Mac
- Synology share mounts but shows read-only permissions
- Synology Finder discovery not working on network

## Prevent It

- Enable SMB 2/3 on Synology DSM for best macOS compatibility
- Keep Synology DSM updated to latest firmware version
- Configure Mac and Synology on same network subnet
- Add Synology hostname to /etc/hosts for reliable discovery
