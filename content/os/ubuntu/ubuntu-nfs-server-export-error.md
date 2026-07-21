---
title: "Ubuntu NFS Server Export Error"
description: "NFS server cannot export directories to clients"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu NFS Server Export Error

NFS server cannot export directories to clients

## Common Causes

- /etc/exports syntax error
- Export directory does not exist
- nfs-kernel-server service not running
- Firewall blocking NFS ports

## How to Fix

1. Check exports: `sudo exportfs -v`
2. Validate: `sudo exportfs -ra` (re-export all)
3. Check service: `systemctl status nfs-kernel-server`
4. Check firewall: `sudo ufw status | grep 2049`

## Examples

```bash
# Check current exports
sudo exportfs -v

# Re-export after editing /etc/exports
sudo exportfs -ra

# Restart NFS server
sudo systemctl restart nfs-kernel-server
```
