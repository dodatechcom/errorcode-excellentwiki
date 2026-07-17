---
title: "Registry is Corrupted Error - How to Fix"
description: "Fix 'Registry is corrupted' errors on Windows 10 and 11. Repair corrupt registry hives, restore system stability, and recover from registry damage."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["registry", "corrupted", "corrupt", "hive", "repair"]
weight: 5
---

# Registry is Corrupted Error

This error occurs when registry hive files are damaged or inconsistent. Symptoms include:

- Applications failing to launch
- Blue screen errors referencing `0xC000021A`
- Windows failing to boot
- System instability and random crashes

Registry hives are stored as binary files in `%SystemRoot%\System32\config\`. Corruption can cause cascading system failures.

## Common Causes

- **Power loss during registry write** — abrupt shutdown corrupted the hive file.
- **Disk errors** — bad sectors damaged the registry files.
- **Malware** — malicious software corrupted or replaced registry entries.
- **Failed Windows update** — interrupted update damaged registry.
- **Registry cleaner tools** — aggressive cleaning removed critical entries.

## How to Fix

### Run System File Checker

```cmd
sfc /scannow
```

### Run DISM to Repair System Image

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check Disk for Errors

```cmd
chkdsk C: /f /r
```

Restart required if checking the system drive.

### Restore from Automatic Registry Backup

If periodic backup is enabled:

```cmd
xcopy /y /h "C:\Windows\System32\config\RegBack\*" "C:\Windows\System32\config\"
```

### Use System Restore

```powershell
Get-ComputerRestorePoint
Restore-Computer -RestorePoint "Restore Point Name"
```

### Boot into Recovery for Full Repair

1. Boot from Windows installation media.
2. Select **Repair your computer**.
3. Choose **Startup Repair**.
4. If that fails, use **Command Prompt**:

```cmd
bootrec /fixmbr
bootrec /fixboot
bootrec /rebuildbcd
```

### Manual Hive Repair from Recovery

```cmd
diskpart
list volume
exit
```

```cmd
ren D:\Windows\System32\config\SYSTEM SYSTEM.old
copy D:\Windows\System32\config\RegBack\SYSTEM D:\Windows\System32\config\SYSTEM
```

## Related Errors

- [Registry Hive Error]({{< relref "/os/windows/reg-hive-error" >}}) — Specific hive file corruption
- [Registry Invalid Data]({{< relref "/os/windows/reg-invalid-data" >}}) — Corrupt values within hives
- [BSOD 0xC000021A]({{< relref "/os/windows/0xc000021a" >}}) — System process failure from registry corruption
