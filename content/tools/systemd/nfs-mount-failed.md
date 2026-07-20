---
title: "[Solution] systemd NFS mount failed"
description: "Fix systemd NFS mount failed. Resolve NFS mount failures from systemd mount units."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd NFS mount failed

## Error Description

mnt-nfs.mount: Mount failed: mount.nfs: No route to host

The NFS mount could not connect to the NFS server.

## Common Causes

Common Causes:
- NFS server is down or unreachable
- NFS export does not exist
- Client IP is not authorized in exports file
- NFS version mismatch

## How to Fix

How to Fix:
```bash
# Test NFS connectivity
showmount -e nfs-server

# Check NFS service
rpcinfo -p nfs-server

# Test mount manually
sudo mount -t nfs nfs-server:/export /mnt/nfs

# Check firewall
sudo firewall-cmd --list-services | grep nfs
```

## Examples

```bash
# Check systemd version
systemctl --version

# Verify unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Analyze system boot
systemd-analyze blame

# List failed units
systemctl --failed

# View service logs
journalctl -u myapp -n 50 --no-pager
```