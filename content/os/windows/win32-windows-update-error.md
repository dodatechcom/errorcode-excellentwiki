---
title: "Windows Update Error 0x80070002 - How to Fix"
description: "Fix Windows Update error 0x80070002 on Windows 10 and 11. Resolve update download failures, fix corrupt update cache, and restore Windows Update functionality."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["windows-update", "0x80070002", "update-error", "update-failed"]
weight: 5
---

# Windows Update Error 0x80070002

This error occurs when Windows Update fails to find or download an update package. The error code is `0x80070002` (ERROR_FILE_NOT_FOUND). The full message reads:

> "There were problems installing some updates, but we'll try again later."

This is one of the most common Windows Update errors, appearing when update files are missing, corrupt, or the update cache is damaged.

## Common Causes

- **Corrupt update cache** — Downloaded update files are damaged.
- **Missing update files** — Windows Update catalog entry exists but files are missing.
- **Date/time incorrect** — System clock mismatch causes certificate validation failure.
- **Antivirus blocking** — Security software blocking update downloads.
- **Windows Update service stopped** — Required services not running.

## How to Fix

### Run Windows Update Troubleshooter

```powershell
ms-settings:troubleshoot
```

Or via command line:

```cmd
msdt.exe /id WindowsUpdateDiagnostic
```

### Clear Windows Update Cache

```cmd
net stop wuauserv
net stop bits
net stop cryptsvc
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
ren C:\Windows\System32\catroot2 catroot2.old
net start cryptsvc
net start bits
net start wuauserv
```

### Run DISM and SFC

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check Date and Time

```powershell
Get-Date
w32tm /query /status
```

### Reset Windows Update Components

```powershell
Stop-Service wuauserv -Force
Stop-Service bits -Force
Stop-Service cryptsvc -Force
Stop-Service appidsvc -Force

Remove-Item "C:\Windows\SoftwareDistribution\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "C:\Windows\System32\catroot2\*" -Recurse -Force -ErrorAction SilentlyContinue

Start-Service wuauserv
Start-Service bits
Start-Service cryptsvc
Start-Service appidsvc
```

### Run Windows Update Manually

```powershell
$session = New-Object -ComObject Microsoft.Update.Session
$searcher = $session.CreateUpdateSearcher()
$updates = $searcher.Search("IsInstalled=0")
$updates.Updates | Select-Object Title, DatePublished
```

### Check Windows Update Logs

```powershell
Get-WinEvent -LogName "Microsoft-Windows-WindowsUpdateClient/Operational" -MaxEvents 20 | Format-List TimeCreated, Message
```

## Related Errors

- [Windows Update Timeout]({{< relref "/os/windows/win32-windows-update-timeout" >}}) — Update process timed out
- [Windows Update Corrupted]({{< relref "/os/windows/win32-windows-update-corrupt" >}}) — Corrupt update files
- [0x8024402C]({{< relref "/os/windows/0x8024402c" >}}) — Windows Update proxy error
