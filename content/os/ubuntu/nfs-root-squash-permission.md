---
title: "NFS Root Squash Permission Denied"
description: "NFS client cannot write to share due to root squashing"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# NFS Root Squash Permission Denied

NFS client cannot write to share due to root squashing

## Common Causes

- Root squash maps root to nobody (65534)
- no_root_squash not enabled in /etc/exports
- Client UID/GID does not match allowed user on server
- File permissions on server not allowing group write

## How to Fix

1. Check exports: `cat /etc/exports`
2. Enable no_root_squash if needed: `no_root_squash` in export line
3. Ensure client user UID matches server UID
4. Reload exports: `sudo exportfs -ra`

## Examples

```bash
# On NFS server, check exports
cat /etc/exports
# Example: /export 192.168.1.0/24(rw,sync,no_subtree_check,no_root_squash)

# Reload exports
sudo exportfs -ra
```
