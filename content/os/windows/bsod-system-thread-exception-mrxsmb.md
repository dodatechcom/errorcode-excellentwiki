---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION mrxsmb.sys Fix"
description: "Fix SYSTEM_THREAD_EXCEPTION caused by mrxsmb.sys on Windows. Resolve SMB mini-redirector driver crash and network file access BSOD errors."
platforms: ["windows"]
severities: ["error"]
error_types: ["bsod"]
weight: 10
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION mrxsmb.sys Fix

The SYSTEM_THREAD_EXCEPTION referencing mrxsmb.sys indicates a crash in the SMB mini-redirector driver responsible for network file sharing. This driver manages SMB protocol operations for accessing files on network shares.

## Common Causes
- SMB client driver bug with specific server configurations
- Network disconnection during active SMB file operations
- Corrupted SMB redirector from Windows updates
- Third-party SMB protocol modification tools
- Authentication timeout during long SMB operations

## How to Fix

### Solution 1: Reset SMB Components

```cmd
net stop lanmanworkstation
net stop lanmanserver
net start lanmanworkstation
net start lanmanserver
```

### Solution 2: Update Network Adapter Driver

```powershell
Get-NetAdapter | Select-Object Name, InterfaceDescription, DriverVersion
```

### Solution 3: Disable SMB Signing if Excessive

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" /v RequireSecuritySignature /t REG_DWORD /d 0 /f
```

### Solution 4: Clear DNS Cache

```cmd
ipconfig /flushdns
nbtstat -R
```

### Solution 5: Check SMB Client Statistics

```powershell
Get-SmbConnection | Select-Object ServerName, ShareName, Dialect, Status
```

## Examples
```powershell
Get-SmbConnection | Select-Object ServerName, ShareName, Dialect, Status
Get-SmbMapping | Select-Object LocalPath, RemotePath, Status
```
