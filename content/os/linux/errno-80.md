---
title: "[Solution] Linux ESTALE (errno 80) — Stale File Handle Fix"
description: "Fix Linux ESTALE (errno 80) Stale file handle error. Solutions for NFS and distributed filesystem stale handle issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["estale", "stale", "errno-80", "nfs", "file-handle"]
weight: 5
---

# Linux ESTALE (errno 80) — Stale File Handle

ESTALE (errno 80) means the file handle is stale and no longer valid. This error typically occurs on NFS-mounted filesystems when the file handle has become stale due to the file being deleted or renamed on the server, or the NFS server was restarted. It is distinct from ENOENT (errno 2) because ESTALE indicates the handle was once valid but is now stale.

## Common Causes

- File was deleted or renamed on the NFS server while open on the client
- NFS server was restarted, invalidating all file handles
- NFS export was reconfigured on the server
- Network partition caused handle to become stale

## How to Fix ESTALE

### 1. Close and Reopen the File

The simplest fix is to close the stale handle and reopen:

```bash
# Close the file descriptor and reopen
close(fd);
fd = open("/mnt/nfs/file.txt", O_RDONLY);
```

### 2. Remount the NFS Share

Clear all stale handles by remounting:

```bash
sudo umount -f /mnt/nfs_share
sudo mount -t nfs server:/share /mnt/nfs_share
```

### 3. Use NFSv4

NFSv4 handles stale connections better:

```bash
sudo mount -t nfs4 server:/share /mnt/nfs
```

### 4. Use Soft Mount with Recovery

Configure NFS mount with appropriate options:

```bash
sudo mount -t nfs -o soft,timeo=30,retrans=3 server:/share /mnt/nfs
```

### 5. Handle Stale Handles in Applications

Detect and retry on ESTALE:

```bash
# In C: retry on ESTALE
if (errno == ESTALE) {
    close(fd);
    fd = open(path, flags);
}
```

## Verification

After remounting, confirm file access works:

```bash
ls -la /mnt/nfs_share/
cat /mnt/nfs_share/file.txt
```

## Related Error Codes

- [ENOLINK (errno 31)](/os/linux/errno-31/) — Link has been severed
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
- [EREMOTEIO (errno 53)](/os/linux/errno-53/) — Remote I/O error
