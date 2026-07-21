---
title: "[Solution] SMB Legacy Protocol Not Supported Error Fix"
description: "Fix SMB legacy protocol not supported error when connecting to older file servers. Resolve SMBv1 compatibility issues on modern Windows systems."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] SMB Legacy Protocol Not Supported Error Fix

The SMB legacy protocol not supported error occurs when modern Windows systems refuse to connect using SMBv1 for security reasons. Older file servers and NAS devices may only support SMBv1.

## Common Causes
- SMBv1 disabled by default on Windows 10 and 11
- Legacy NAS or file server only supports SMBv1
- Group Policy disabling SMBv1 for security hardening
- Windows update removing SMBv1 components
- Third-party SMB implementation not supporting SMBv2

## How to Fix

### Solution 1: Check SMBv1 Status

```powershell
Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol
Get-SmbClientConfiguration | Select-Object EnableSMB1Protocol
```

### Solution 2: Enable SMBv1 on Client

```powershell
Set-SmbClientConfiguration -EnableSMB1Protocol $true -Force
```

Only enable for legacy device compatibility and disable after upgrading.

### Solution 3: Upgrade Legacy Devices

Update firmware on NAS and file servers to support SMBv2 or SMBv3.

### Solution 4: Enable SMBv1 on Server

```powershell
Set-SmbServerConfiguration -EnableSMB1Protocol $true -Force
```

### Solution 5: Use Third-Party SMB Client

For devices that cannot be upgraded, consider using a third-party SMB client that supports legacy protocols.

## Examples
```powershell
Get-SmbConnection | Select-Object ServerName, Dialect, EncryptData
Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol, EnableSMB2Protocol
```
