---
title: "NFS ID Mapping Error"
description: "NFS client maps incorrect user/group IDs for files"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# NFS ID Mapping Error

NFS client maps incorrect user/group IDs for files

## Common Causes

- id_resolver not configured in nfs.conf
- UID/GID do not match between client and server
- nfsidmap service not running
- Name service (nsswitch) not configured for NFS

## How to Fix

1. Check id_resolver: `grep -r id_resolver /etc/nfs.conf`
2. Enable: `id_resolver = yes` in /etc/nfs.conf
3. Check mapping: `nfsidmap -c`
4. Restart: `sudo systemctl restart nfs-idmapd`

## Examples

```bash
# Check NFS id mapping config
grep -A5 '\[nfsd\]' /etc/nfs.conf

# Enable id_resolver
sudo sed -i 's/#id_resolver = no/id_resolver = yes/' /etc/nfs.conf

# Restart id mapping service
sudo systemctl restart nfs-idmapd
```
