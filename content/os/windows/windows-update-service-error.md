---
title: "[Solution] Windows Update Service Not Running Fix"
description: "Fix Windows Update service not running on Windows 10 and 11. Resolve wuauserv service failures with service restarts, dependency fixes, and registry repairs."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
weight: 5
---

# [Solution] Windows Update Service Not Running Fix

The Windows Update service (wuauserv) has stopped running or cannot start. This prevents Windows from checking for, downloading, or installing updates. The service may fail to start due to corrupted files, dependency issues, or registry problems.

This error appears when you try to check for updates and receive a message that the service is not running or cannot be started.

## What This Error Means

The error typically appears as:

> "There were problems checking for updates. Error code: 0x80070424"
> "Windows Update service is not running."

Or in services.msc, the Windows Update service shows as **Stopped** or **Disabled**.

The Windows Update service depends on several other services. If any dependency fails, wuauserv cannot start. Common causes include:

- **Service dependencies stopped** — Background Intelligent Transfer Service or Cryptographic Services not running
- **Corrupted service registry entries** — Damaged registry entries for the wuauserv service
- **Malware disabling services** — Malware stopping the update service
- **Third-party software interference** — Software that disables Windows Update

## Common Causes

1. **Service dependencies stopped** — BITS or Cryptographic Services not running.
2. **Corrupted service registry** — Damaged registry entries for the wuauserv service.
3. **Malware** — Malware disabling the update service.
4. **Third-party software** — Software blocking Windows Update.

## How to Fix

### Start All Required Services

```cmd
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

If any service fails to start, check its dependencies:

```cmd
sc query wuauserv
sc qc wuauserv
```

### Reset Windows Update Components

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
regsvr32 /s atl.dll
regsvr32 /s urlmon.dll
regsvr32 /s mshtml.dll
regsvr32 /s shdocvw.dll
regsvr32 /s browseui.dll
regsvr32 /s jscript.dll
regsvr32 /s vbscript.dll
regsvr32 /s scrrun.dll
regsvr32 /s msxml.dll
regsvr32 /s msxml3.dll
regsvr32 /s msxml6.dll
regsvr32 /s actxprxy.dll
regsvr32 /s softpub.dll
regsvr32 /s wintrust.dll
regsvr32 /s dssenh.dll
regsvr32 /s rsaenh.dll
regsvr32 /s gpkcsp.dll
regsvr32 /s sccbase.dll
regsvr32 /s slbcsp.dll
regsvr32 /s cryptdlg.dll
regsvr32 /s oleaut32.dll
regsvr32 /s ole32.dll
regsvr32 /s shell32.dll
regsvr32 /s wuaueng.dll
regsvr32 /s wuaueng1.dll
regsvr32 /s wucltui.dll
regsvr32 /s wups.dll
regsvr32 /s wups2.dll
regsvr32 /s wuweb.dll
regsvr32 /s qmgr.dll
regsvr32 /s qmgrprxy.dll
regsvr32 /s wucltux.dll
regsvr32 /s muweb.dll
regsvr32 /s wuwebv.dll
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

### Re-register Windows Update DLLs

```cmd
net stop wuauserv
regsvr32 /s wuaueng.dll
regsvr32 /s wuaueng1.dll
regsvr32 /s wucltui.dll
regsvr32 /s wups.dll
regsvr32 /s wuweb.dll
net start wuauserv
```

### Check Service Startup Type

```powershell
Get-Service wuauserv | Select-Object Name, Status, StartType
```

If the service is disabled, enable it:

```powershell
Set-Service -Name wuauserv -StartupType Automatic
Start-Service -Name wuauserv
```

### Run Windows Update Troubleshooter

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter.

### Check for Malware

```powershell
Start-MpScan -ScanType FullScan
```

## Related Errors

- [Error 0x80070005]({{< relref "/os/windows/windows-update-0x80070005" >}}) — Access Denied
- [Error 0x80070002]({{< relref "/os/windows/windows-update-0x80070002" >}}) — File Not Found
- [Windows Update Stuck]({{< relref "/os/windows/windows-update-stuck" >}}) — Update stuck at downloading/installing
