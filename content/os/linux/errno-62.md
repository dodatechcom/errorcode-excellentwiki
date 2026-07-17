---
title: "[Solution] Linux EREMOTE (errno 62) — Object Is Remote Fix"
description: "Fix Linux EREMOTE (errno 62) Object is remote error. Solutions for remote object access issues on network storage."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EREMOTE (errno 62) — Object Is Remote

EREMOTE (errno 62) means the object is remote and the operation cannot be performed. This error occurs when a program attempts an operation that is not supported on remote filesystems, such as certain `ioctl()` calls or advisory locking on NFS-mounted files. It is distinct from ENOLINK (errno 31) because EREMOTE indicates the object itself is remote, not that a connection was lost.

## Common Causes

- Attempting local-only operations on NFS-mounted files
- Using `ioctl()` on remote file descriptors
- Advisory file locking over NFS without proper options
- Trying to create device nodes on remote filesystems

## How to Fix EREMOTE

### 1. Identify Remote Filesystems

Check which paths are on remote filesystems:

```bash
df /path/to/file
mount | grep -E "nfs|cifs|fuse"
```

### 2. Copy Files to Local Storage

For operations requiring local access, copy files locally:

```bash
cp /mnt/nfs/remote_file /tmp/local_file
# Perform operation on local copy
```

### 3. Use NFS-Compatible Operations

Use operations that are supported over NFS:

```bash
# Use flock-compatible NFS mounts
sudo mount -t nfs -o lock server:/share /mnt/nfs
```

### 4. Use NFSv4

NFSv4 supports more operations than earlier versions:

```bash
sudo mount -t nfs4 server:/share /mnt/nfs
```

## Verification

After applying the fix, confirm the operation succeeds:

```bash
strace -e trace=open,ioctl,fcntl ./program
```

## Related Error Codes

- [ENOLINK (errno 31)](/os/linux/errno-31/) — Link has been severed
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
- [ENOTCONN (errno 71)](/os/linux/errno-71/) — Not connected
