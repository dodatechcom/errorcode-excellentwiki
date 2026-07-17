---
title: "[Solution] Linux ENOLINK (errno 31) — Link Has Been Severed Fix"
description: "Fix Linux ENOLINK (errno 31) Link has been severed error. Solutions for stale NFS and distributed filesystem issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENOLINK (errno 31) — Link Has Been Severed

ENOLINK (errno 31) means the link to a remote machine has been severed or the file system was unmounted. This error typically occurs in NFS and other distributed filesystem environments when the connection to the server is lost while a file is open. It is distinct from ESTALE (errno 112) because ENOLINK refers specifically to a broken network link.

## Common Causes

- NFS server became unreachable during an operation
- Network connection dropped while accessing a remote file
- The remote filesystem was unmounted while files were open
- Distributed filesystem node failure

## How to Fix ENOLINK

### 1. Check Network Connectivity

Verify the connection to the remote server:

```bash
ping nfs-server.example.com
```

### 2. Verify NFS Mount Status

Check if the NFS mount is still active:

```bash
mount | grep nfs
nfsstat -c
```

### 3. Remount the NFS Share

Remount the NFS share to re-establish the connection:

```bash
sudo umount -f /mnt/nfs_share
sudo mount -t nfs server:/share /mnt/nfs_share
```

### 4. Use Hard Mounts for Reliability

Use hard mounts instead of soft mounts to prevent ENOLINK:

```bash
sudo mount -t nfs -o hard,intr server:/share /mnt/nfs_share
```

### 5. Check NFS Server Status

Ensure the NFS server is running:

```bash
sudo systemctl status nfs-server
showmount -e server.example.com
```

## Verification

After remounting, confirm access works:

```bash
ls /mnt/nfs_share/
```

## Related Error Codes

- [ESTALE (errno 80)](/os/linux/errno-80/) — Stale file handle
- [ENOTCONN (errno 107)](/os/linux/errno-71/) — Not connected
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
