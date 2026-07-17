---
title: "[Solution] BSOD CRITICAL_PROCESS_DIED — 0xEF ci.dll Windows 11/10"
description: "Fix Blue Screen CRITICAL_PROCESS_DIED stop code 0xEF caused by ci.dll Code Integrity on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD CRITICAL_PROCESS_DIED — 0xEF ci.dll

The `CRITICAL_PROCESS_DIED` stop code `0xEF` with `ci.dll` indicates the Code Integrity module terminated unexpectedly. CI.dll is responsible for verifying driver and system file signatures. Its failure prevents Windows from validating the integrity of loaded components.

## Common Causes

- **Corrupted ci.dll** — The Code Integrity module is damaged by disk errors or malware.
- **Unsigned driver loaded** — A driver without valid signature causes CI to crash.
- **Failed Windows update** — An update corrupts the code integrity components.
- **Disk corruption affecting system files** — Bad sectors prevent CI.dll from loading correctly.

## How to Fix

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check for Unsigned Drivers

```powershell
Get-WindowsDriver -Online | Where-Object { $_.SignatureStatus -ne "Signed" } | Select-Object OriginalFileName, ProviderName, Date, Version
```

### Boot into Safe Mode

```cmd
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

Uninstall recently installed drivers in Safe Mode.

### Run Check Disk

```cmd
chkdsk C: /f /r
```

### Restore ci.dll from Installation Media

```cmd
# Mount Windows ISO and copy ci.dll
copy D:\Sources\install.wim C:\Windows\System32\ci.dll
```

### Update Windows

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -Install -AcceptAll
```

## Examples

```text
CRITICAL_PROCESS_DIED (ef)
A critical system process terminated unexpectedly.

MODULE_NAME: CI
IMAGE_NAME:  CI.dll
```

## Related Errors

- [BSOD CRITICAL_PROCESS_DIED storport.sys]({{< relref "/os/windows/bsod-critical-process-died3" >}}) — Storage port failure
- [BSOD CRITICAL_PROCESS_DIED win32kfull.sys]({{< relref "/os/windows/bsod-critical-process-died5" >}}) — Win32k critical failure
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED CI.dll]({{< relref "/os/windows/bsod-system-thread-exception7" >}}) — CI.dll thread exception
