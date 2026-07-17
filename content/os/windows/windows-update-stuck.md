---
title: "[Solution] Windows Update Stuck at Downloading or Installing Fix"
description: "Fix Windows Update stuck at downloading or installing on Windows 10 and 11. Resolve frozen updates with BITS resets, safe mode installs, and manual update methods."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
weight: 5
---

# [Solution] Windows Update Stuck at Downloading or Installing Fix

Windows Update is stuck at a certain percentage during downloading or installing, with no progress for an extended period. The update agent appears frozen and does not complete or fail.

This is one of the most common Windows Update issues. The update may be stuck at 0%, 20%, 40%, or any other percentage, and the progress indicator does not advance for more than 30 minutes.

## What This Error Means

The update process shows:

> "Downloading updates — 0%"
> or
> "Installing updates — XX%"
> with no progress for an extended period.

Common causes of stuck updates:

- **BITS queue corruption** — Background Intelligent Transfer Service queue has stuck jobs
- **Large update download** — Cumulative updates can be several GB and take time
- **Slow internet connection** — Insufficient bandwidth for large downloads
- **Disk space issues** — Not enough space for the update installation
- **Conflicting software** — Third-party software interfering with the update process

## Common Causes

1. **BITS queue corruption** — Stuck download jobs preventing new downloads.
2. **Insufficient disk space** — Not enough space for download or installation.
3. **Slow or unstable internet** — Bandwidth issues causing timeouts.
4. **Third-party antivirus** — Security software blocking update operations.
5. **Corrupted update cache** — Damaged SoftwareDistribution folder.

## How to Fix

### Wait at Least 60 Minutes

Before making changes, wait at least 60 minutes. Large cumulative updates can take a long time to download and install, especially on slow connections.

### Check Disk Space

```powershell
Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{N='Used(GB)';E={[math]::Round($_.Used/1GB,2)}}, @{N='Free(GB)';E={[math]::Round($_.Free/1GB,2)}} | Format-Table -AutoSize
```

Ensure at least **20 GB** of free space on the system drive.

### Restart BITS Service

```cmd
net stop bits
net start bits
```

**Check BITS queue:**

```cmd
bitsadmin /list /allusers
```

**Clear stuck BITS jobs:**

```cmd
bitsadmin /reset /allusers
```

### Reset Windows Update Cache

```cmd
net stop wuauserv
net stop bits
net stop cryptSvc
net stop msiserver
rd /s /q "C:\Windows\SoftwareDistribution"
net start wuauserv
net start bits
net start cryptSvc
net start msiserver
```

### Run Windows Update in Safe Mode

1. Press `Win + R`, type `msconfig`, and press Enter.
2. Go to the **Boot** tab and check **Safe boot**.
3. Select **Network** and click **OK**.
4. Restart the computer.
5. Run Windows Update in Safe Mode.
6. After the update completes, run `msconfig` and uncheck **Safe boot**.

### Install Updates Using PowerShell

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
```

### Manually Install the Update

1. Note the KB number from Windows Update.
2. Visit [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Download the correct version for your system.
4. Run the installer and restart when prompted.

### Clear BITS Jobs and Retry

```cmd
bitsadmin /reset /allusers
net stop bits
net start bits
wuauclt /detectnow
wuauclt /updatenow
```

## Related Errors

- [Windows Update Service Error]({{< relref "/os/windows/windows-update-service-error" >}}) — Update service not running
- [Error 0x800f0922]({{< relref "/os/windows/windows-update-0x800f0922" >}}) — Connection timeout
- [Error 0x8024402f]({{< relref "/os/windows/windows-update-0x8024402f" >}}) — Download error
