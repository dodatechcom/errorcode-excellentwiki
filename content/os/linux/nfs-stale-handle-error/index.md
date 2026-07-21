---
title: "Fix Linux: nfs-stale-handle-error -- NFS stale file handle error in Linux"
description: "Resolve NFS stale file handle errors preventing file access on Linux systems."
os: ["linux"]
error-types: [["network", "filesystem"]]
severities: [["error", "warning"]]
---

NFS stale file handle errors occur when the server inode no longer matches the client handle, usually after server-side changes.

## Common Causes
- File or directory deleted on NFS server
- Server re-exported after rebuild
- NFS re-export of underlying filesystem
- Server inode number changed

## How to Fix
1. Verify the file exists on the server:
   ls -la /export/path/
2. Remount the NFS share:
   umount /mnt/nfs && mount -t nfs server:/export /mnt/nfs
3. Clear client cache:
   echo 3 > /proc/sys/vm/drop_caches
4. Use noac mount option for critical apps:
   mount -t nfs -o noac server:/export /mnt/nfs

## Examples
### Common Error Message
NFS: file handle does not exist\n
Stale file handle
