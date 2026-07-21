---
title: "Ubuntu NFS Mount Error on Boot"
description: "NFS mount configured in fstab fails during system boot"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu NFS Mount Error on Boot

NFS mount configured in fstab fails during system boot

## Common Causes

- Network not ready when fstab NFS mount attempted
- NFS server not responding during boot sequence
- x-systemd.automount not configured
- NFS mount timeout exceeded during boot

## How to Fix

1. Check fstab: `grep nfs /etc/fstab`
2. Add x-systemd.automount: `server:/export /mnt/nfs nfs defaults,x-systemd.automount,_netdev 0 0`
3. Test mount: `sudo mount -a`
4. Check automount: `systemctl list-units | grep mnt-nfs`

## Examples

```bash
# Example fstab entry with automount
# 192.168.1.100:/share /mnt/nfs nfs defaults,x-systemd.automount,_netdev,x-systemd.idle-timeout=30 0 0

# Mount all fstab entries
sudo mount -a

# Check automount status
systemctl list-units | grep mnt
```
