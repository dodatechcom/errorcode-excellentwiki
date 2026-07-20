---
title: "[Solution] Linux: disk-nfs-error — NFS mount error"
description: "Fix Linux disk-nfs-error errors. NFS mount error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: NFS Mount Error

NFS errors occur when mounting or accessing remote filesystems over the Network File System protocol.

## Common Causes

- NFS server not running or firewall blocking port 2049
- Export not configured in /etc/exports or permissions too restrictive
- NFS client missing required services (rpcbind, nfs-common)
- Network connectivity or routing issues between client and server
- NFS version mismatch

## How to Fix

### 1. Check Server Exports

```bash
showmount -e <server>
rpcinfo -p <server>
```

### 2. Check NFS Service on Server

```bash
sudo systemctl status nfs-kernel-server  # Debian/Ubuntu
sudo systemctl status nfs-server          # RHEL/CentOS
```

### 3. Mount with Options

```bash
sudo mount -t nfs4 <server>:/export /mnt
sudo mount -t nfs -o vers=3 <server>:/export /mnt
sudo mount -t nfs -o rw,hard,intr,timeo=30,retrans=3 <server>:/export /mnt
```

## Examples

```bash
$ showmount -e nfsserver
Export list for nfsserver:
/data *(rw,sync,no_subtree_check)

$ sudo mount -t nfs4 nfsserver:/data /mnt
mount.nfs4: Connection refused
```
