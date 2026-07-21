---
title: "NFSv4 File Locking Error"
description: "NFSv4 file locking fails causing application errors"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# NFSv4 File Locking Error

NFSv4 file locking fails causing application errors

## Common Causes

- NFSv4 delegation not working
- Lock daemon not running on client or server
- File locks conflicting between multiple clients
- NFS server not supporting advisory locking

## How to Fix

1. Check lock status: `nfsstat -c`
2. Test locks: `flock -n /mnt/nfs/testfile echo 'lock acquired'`
3. Check nfsd: `systemctl status nfs-server`
4. Mount with lock option: `mount -o lock,nfsvers=4`

## Examples

```bash
# Test file locking on NFS mount
flock -n /mnt/nfs/testfile echo 'lock acquired'

# Check NFS statistics
nfsstat -c

# Mount NFS with explicit lock option
sudo mount -t nfs4 -o lock server:/export /mnt/nfs
```
