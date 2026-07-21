---
title: "Samba Authentication Failed Error"
description: "SMB client cannot authenticate to Samba share"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Samba Authentication Failed Error

SMB client cannot authenticate to Samba share

## Common Causes

- Samba password not set or different from system password
- User not added to Samba password database
- SMB encrypted passwords required but client sending plaintext
- Domain membership expired or invalid

## How to Fix

1. Set Samba password: `sudo smbpasswd -a username`
2. Check Samba users: `pdbedit -L`
3. Verify user exists in system: `id username`
4. Test connection: `smbclient -L localhost -U username`

## Examples

```bash
# Add user to Samba
sudo smbpasswd -a admin

# List Samba users
sudo pdbedit -L

# Test local connection
smbclient -L localhost -U admin
```
