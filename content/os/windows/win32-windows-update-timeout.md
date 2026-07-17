---
title: "Windows Update Timeout Error - How to Fix"
description: "Fix Windows Update timeout errors on Windows 10 and 11. Resolve stuck updates, increase timeout limits, and fix update download/installation hangs."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Windows Update Timeout Error

This error occurs when Windows Update takes too long to download or install an update, exceeding the system's timeout threshold. The error may read:

> "We couldn't complete the updates. Undoing changes."

or

> "Windows Update is taking too long."

This commonly appears with large feature updates, slow internet connections, or when the update process hangs.

## Common Causes

- **Slow internet connection** — Large update files downloading slowly.
- **Windows Update service hung** — Service stopped responding.
- **Disk I/O bottleneck** — Slow disk can't keep up with update installation.
- **Conflicting software** — Antivirus or other software interfering with update process.
- **Insufficient disk space** — Not enough space for update extraction.

## How to Fix

### Check Internet Connection Speed

```powershell
Test-NetConnection -ComputerName "download.windowsupdate.com" -Port 443
```

### Restart Windows Update Services

```powershell
Restart-Service wuauserv -Force
Restart-Service bits -Force
```

### Increase Service Timeout

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control" /v "ServicesPipeTimeout" /t REG_DWORD /d 180000 /f
```

Restart after making this change.

### Check Disk Space

```powershell
Get-PSDrive C | Select-Object @{N="Free(GB)";E={[math]::Round($_.Free/1GB,2)}}, @{N="Used(GB)";E={[math]::Round($_.Used/1GB,2)}}
```

### Run Update in Clean Boot State

```cmd
msconfig
```

Go to **Services** tab, check **Hide all Microsoft services**, click **Disable all**. Go to **Startup** tab, click **Open Task Manager** and disable all startup items. Restart and run Windows Update.

### Use Windows Update Catalog Manually

1. Note the KB number from Windows Update.
2. Go to https://www.catalog.update.microsoft.com.
3. Search for the KB number.
4. Download the correct version.
5. Install manually.

### Check Update Progress

```powershell
Get-WinEvent -LogName "Microsoft-Windows-WindowsUpdateClient/Operational" -MaxEvents 10 | Format-List TimeCreated, Message
```

### Use DISM to Service Windows

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

## Related Errors

- [Windows Update Error 0x80070002]({{< relref "/os/windows/win32-windows-update-error" >}}) — Update files not found
- [Windows Update Corrupted]({{< relref "/os/windows/win32-windows-update-corrupt" >}}) — Corrupt update files
- [ERROR_TIMEOUT (1460)]({{< relref "/os/windows/win32-timeout-win32" >}}) — General timeout error
