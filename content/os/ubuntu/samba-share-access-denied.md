---
title: "[Solution] Ubuntu Server: samba-share-access-denied"
description: "Fix Ubuntu samba-share-access-denied. Samba share access is denied for connecting clients."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Samba Share Access Denied

Samba denies access to file shares from Windows or Linux clients.

## Common Causes
- Invalid username or password
- Share not accessible by user
- Map to guest option misconfigured
- NTLM authentication disabled
- Guest account not set properly

## How to Fix
1. Check Samba users
```bash
sudo pdbedit -L
```
2. Add user to Samba
```bash
sudo smbpasswd -a <username>
```
3. Check share permissions
```bash
testparm -s | grep -A5 "path"
```

## Examples
```bash
$ sudo pdbedit -L
john:1001

$ sudo smbpasswd -a john
New SMB password:
Retype new SMB password:
```
