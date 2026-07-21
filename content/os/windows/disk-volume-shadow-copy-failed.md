---
title: "[Solution] Volume Shadow Copy Service Error Fix"
description: "Fix Windows Volume Shadow Copy Service errors preventing system restore points and backups. Resolve VSS writer failures and snapshot issues on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Volume Shadow Copy Service Error Fix

The Volume Shadow Copy Service (VSS) manages the creation of shadow copies for backups and restore points. When VSS fails, system restore, backup operations, and snapshot creation all stop working.

## Common Causes
- VSS writer in a failed state from a previous operation
- Insufficient disk space for shadow copy storage
- Corrupted VSS registry entries
- Third-party backup software conflicting with VSS
- System Writer or BITS Writer in error state

## How to Fix

### Solution 1: Check VSS Writer Status

```cmd
vssadmin list writers
```

### Solution 2: Restart VSS Service

```powershell
Restart-Service -Name VSS
Restart-Service -Name SWPRV
```

### Solution 3: Re-register VSS Components

```cmd
net stop vsscsvc
net stop swprv
regsvr32 /s ole32.dll
regsvr32 /s oleaut32.dll
regsvr32 /s vss_ps.dll
net start swprv
net start vsscsvc
```

### Solution 4: Check Disk Space

Ensure at least 300 MB of free space on the system drive for shadow copy storage.

### Solution 5: Reset VSS Storage

```cmd
vssadmin resize shadowstorage /for=C: /on=C: /maxsize=10%
```

## Examples
```powershell
vssadmin list writers
vssadmin list shadowstorage
```
