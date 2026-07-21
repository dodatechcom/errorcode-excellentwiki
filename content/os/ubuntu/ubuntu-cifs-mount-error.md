---
title: "Ubuntu CIFS/SMB Mount Error"
description: "SMB/CIFS share mount fails on Ubuntu client"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu CIFS/SMB Mount Error

SMB/CIFS share mount fails on Ubuntu client

## Common Causes

- SMB protocol version mismatch
- Username or password incorrect
- CIFS utils package not installed
- Share does not exist on server

## How to Fix

1. Install: `sudo apt-get install cifs-utils`
2. Test: `smbclient -L //server -U user`
3. Mount: `sudo mount -t cifs //server/share /mnt/smb -o username=user,password=pass`
4. Check protocol: `mount -t cifs -o vers=3.0 //server/share /mnt/smb`

## Examples

```bash
# Install CIFS utilities
sudo apt-get install cifs-utils

# Test SMB connection
smbclient -L //server.example.com -U admin

# Mount SMB share
sudo mount -t cifs //server/share /mnt/smb -o username=admin,password=secret,vers=3.0
```
