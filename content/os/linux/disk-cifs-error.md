---
title: "[Solution] Linux: disk-cifs-error — CIFS/SMB mount error"
description: "Fix Linux disk-cifs-error errors. CIFS/SMB mount error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 6
---
# Linux: CIFS/SMB Mount Error

CIFS errors occur when mounting Windows file shares from Linux using mount.cifs.

## Common Causes

- Incorrect username, password, or domain for the SMB share
- SMB protocol version mismatch (client needs SMB3, server only supports SMB1)
- Network connectivity issues between client and server
- Share name not found or insufficient permissions
- CIFS kernel module not loaded

## How to Fix

### 1. Test Connectivity with smbclient

```bash
smbclient -L //server/share -U username
```

### 2. Mount with Explicit SMB Version

```bash
# Try SMB 3.0
sudo mount -t cifs //server/share /mnt -o username=user,vers=3.0
# Try SMB 2.1
sudo mount -t cifs //server/share /mnt -o username=user,vers=2.1
```

### 3. Use Credentials File

```bash
echo "username=user" > ~/.smbcredentials
echo "password=secret" >> ~/.smbcredentials
chmod 600 ~/.smbcredentials
sudo mount -t cifs //server/share /mnt -o credentials=~/.smbcredentials,vers=3.0
```

### 4. Load CIFS Module

```bash
sudo modprobe cifs
```

## Examples

```bash
$ sudo mount -t cifs //fileserver/shared /mnt -o username=jdoe
mount error(112): Host is down

$ smbclient -L //fileserver -U jdoe
session setup failed: NT_STATUS_CONNECTION_REFUSED

$ ping fileserver
PING fileserver (192.168.1.100) 56(84) bytes of data.
64 bytes from 192.168.1.100: icmp_seq=1 ttl=64 time=0.345 ms
```
