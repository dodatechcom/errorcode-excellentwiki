---
title: "Windows Update Corrupted Files Error - How to Fix"
description: "Fix Windows Update corrupted files errors on Windows 10 and 11. Repair system files, clear corrupt update cache, and restore Windows Update functionality."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["windows-update", "corrupt", "corrupted-files", "repair"]
weight: 5
---

# Windows Update Corrupted Files Error

This error occurs when Windows Update detects corrupted system files or update components. The error may read:

> "We couldn't install some updates because there was a problem."

or

> "Error encountered while installing updates."

Corrupted files can prevent updates from installing correctly and cause system instability.

## Common Causes

- **Interrupted update** — Previous update was interrupted during installation.
- **Disk errors** — Storage corruption damaged system files.
- **Malware damage** — Malicious software corrupted system components.
- **Power loss** — System shutdown during update process.
- **Registry corruption** — Update-related registry entries are damaged.

## How to Fix

### Run System File Checker

```cmd
sfc /scannow
```

### Run DISM to Repair System Image

```cmd
DISM /Online /Cleanup-Image /CheckHealth
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

### Use DISM with Source

```cmd
DISM /Online /Cleanup-Image /RestoreHealth /Source:D:\Sources\install.wim
```

### Repair Windows from Installation Media

1. Boot from Windows installation media.
2. Select **Repair your computer**.
3. Choose **Startup Repair**.
4. If that fails, open **Command Prompt**:

```cmd
sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows
```

### Check Disk for Errors

```cmd
chkdsk C: /f /r
```

### Reset Windows Update Components

```powershell
Stop-Service wuauserv -Force
Stop-Service bits -Force
Stop-Service cryptsvc -Force
Stop-Service appidsvc -Force
Stop-Service msiserver -Force

# Clear update cache
Remove-Item "C:\Windows\SoftwareDistribution\Download\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "C:\Windows\SoftwareDistribution\DataStore\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "C:\Windows\System32\catroot2\*" -Recurse -Force -ErrorAction SilentlyContinue

Start-Service msiserver
Start-Service appidsvc
Start-Service cryptsvc
Start-Service bits
Start-Service wuauserv
```

### Check Windows Event Logs

```powershell
Get-WinEvent -LogName "Microsoft-Windows-WindowsUpdateClient/Operational" -MaxEvents 20 | Where-Object { $_.LevelDisplayName -eq "Error" } | Format-List TimeCreated, Message
```

### Use System Restore

```powershell
Get-ComputerRestorePoint
Restore-Computer -RestorePoint "Before Update"
```

## Related Errors

- [Windows Update Error 0x80070002]({{< relref "/os/windows/win32-windows-update-error" >}}) — Update files missing
- [Windows Update Timeout]({{< relref "/os/windows/win32-windows-update-timeout" >}}) — Update timed out
- [Registry Corrupted]({{< relref "/os/windows/reg-corrupted" >}}) — Registry corruption
