---
title: "[Solution] Windows Update Error 0x80070002 File Not Found Fix"
description: "Fix Windows Update error 0x80070002 (File Not Found) on Windows 10 and 11. Clear the Windows Update cache and fix corrupted system files with these steps."
platforms: ["windows"]
severities: ["error"]
error_types: ["update-error"]
tags: ["windows-update", "file-not-found", "cache", "SoftwareDistribution"]
weight: 5
---

# [Solution] Windows Update Error 0x80070002 File Not Found Fix

Error 0x80070002 is a "File Not Found" error that strikes during Windows Update operations. When Windows searches for update files that don't exist or have been corrupted, it throws this error and blocks the entire update process.

This error affects both Windows 10 and 11 and is usually caused by a corrupted Windows Update cache or mismatched update metadata. The fix is straightforward once you know which cache folders to clear.

## Description

The full error message typically reads:

> "There were problems downloading some updates, but we'll try again later. If you keep seeing this, try searching the web or contacting support for help. Error code: (0x80070002)"

This error occurs when Windows Update's local cache contains references to update files that no longer exist on the Microsoft servers, or when the cached metadata is corrupted. The system tries to locate the file based on cached information, fails, and reports the error.

## Common Causes

- **Corrupted SoftwareDistribution folder** — The Windows Update download cache contains stale or damaged files.
- **Corrupted Catroot2 folder** — The folder that stores Windows Update package signatures is damaged.
- **Interrupted update downloads** — A partial download left corrupt metadata.
- **Incorrect system date/time** — Certificate validation fails when the clock is wrong.

## How to Fix

### Clear the SoftwareDistribution Folder

This is the most effective fix for 0x80070002.

Open **Command Prompt as Administrator** and run:

```cmd
net stop wuauserv
net stop bits
```

Delete the contents of the SoftwareDistribution folder:

```cmd
rd /s /q C:\Windows\SoftwareDistribution
md C:\Windows\SoftwareDistribution
```

Restart the services:

```cmd
net start wuauserv
net start bits
```

Try running Windows Update again.

### Delete the Catroot2 Folder

```cmd
net stop cryptsvc
ren C:\Windows\System32\catroot2 catroot2.old
net start cryptsvc
```

Windows will automatically recreate the Catroot2 folder when you run Windows Update again.

### Run Windows Update Troubleshooter

1. Press `Win + I` to open **Settings**.
2. Navigate to **System > Troubleshoot > Other troubleshooters**.
3. Locate **Windows Update** and click **Run**.

Or from the command line:

```cmd
msdt.exe /id WindowsUpdateDiagnostic
```

### Check Date and Time Settings

1. Press `Win + I` to open **Settings**.
2. Go to **Time & language > Date & time**.
3. Enable **Set time automatically**.
4. Click **Sync now** under "Additional settings."

From the command line:

```cmd
w32tm /resync /force
net time \\time.windows.com /set /yes
```

### Run SFC and DISM

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Full Windows Update Component Reset

For stubborn cases, run these commands in an elevated Command Prompt:

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
net stop appidsvc
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
ren C:\Windows\System32\catroot2 catroot2.old
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate" /v AccountDomainSid /f
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate" /v PingID /f
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate" /v SusClientId /f
netsh winsock reset
net start appidsvc
net start cryptsvc
net start bits
net start wuauserv
net start msiserver
```

## Examples

This error commonly occurs in these scenarios:

- **After an interrupted update** — A partial download left corrupt metadata in the cache.
- **When Microsoft pulls an update** — Cached metadata references a file that no longer exists on Microsoft servers.
- **After running disk cleanup** — Aggressive cleanup tools removing update files without clearing metadata.
- **With incorrect system clock** — Certificate validation fails, causing downloads to fail silently.

## Related Errors

- [Error 0x80004005]({{< relref "/os/windows/0x80004005" >}}) — Unspecified Error, often appears alongside 0x80070002
- [Error 0x80070005]({{< relref "/os/windows/windows-update-0x80070005" >}}) — Access Denied error during Windows Update
- [Error 0x800f081f]({{< relref "/os/windows/0x800f081f" >}}) — Windows could not find required files for .NET Framework
- [Error 0x8024402c]({{< relref "/os/windows/windows-update-0x8024402c" >}}) — Windows Update cannot connect to the update server
