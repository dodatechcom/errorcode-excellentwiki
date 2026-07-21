---
title: "NFS Mount Timeout Error"
description: "NFS client cannot mount or times out connecting to NFS server"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# NFS Mount Timeout Error

NFS client cannot mount or times out connecting to NFS server

## Common Causes

- NFS server not running or unreachable
- Firewall blocking NFS ports (2049, 111, 20048)
- RPC portmapper service not running on server
- NFS export not configured for client IP

## How to Fix

1. Check NFS server: `showmount -e <server>`
2. Verify server status: `rpcinfo -p <server>`
3. Check firewall: `sudo ufw status | grep 2049`
4. Check exports: `cat /etc/exports` on server

## Examples

```bash
# Check NFS exports from server
showmount -e nfs-server.example.com

# Check RPC services
rpcinfo -p nfs-server.example.com

# Mount NFS share with verbose output
sudo mount -v -t nfs nfs-server:/export /mnt/nfs
```
