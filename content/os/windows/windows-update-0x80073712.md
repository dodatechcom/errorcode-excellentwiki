---
title: "[Solution] Windows Update Error 0x80073712 Component Store Fix"
description: "Fix Windows Update error 0x80073712 (component store corrupted) on Windows 10 and 11. Run DISM, repair the component store, and reset Windows Update to resolve."
platforms: ["windows"]
severities: ["error"]
error_types: ["update-error"]
tags: ["windows-update", "component-store", "corrupted", "DISM", "CBS"]
weight: 5
---

# [Solution] Windows Update Error 0x80073712 Component Store Fix

Error 0x80073712 is a Windows Update error that indicates the component store is corrupted. The full error message is `ERROR_WU_E_UNEXPECTED_UPDATE_ENGINE_ERROR` or `CBS_E_STORE_CORRUPTION`. Windows cannot proceed with updates because the Component-Based Servicing (CBS) database is damaged or contains inconsistent data.

This error affects both Windows 10 and 11 and typically blocks cumulative and feature updates from installing. The system cannot reconcile the expected component state with what is actually present on disk.

## Description

The full error message typically reads:

> "There were problems downloading some updates, but we'll try again later. Error code: (0x80073712)"

Or in CBS logs:

> "Error 0x80073712: The component store is corrupted."

The Windows component store (`C:\Windows\WinSxS`) contains the files needed to install, update, and remove Windows features and updates. When this store becomes corrupted — often from interrupted updates, disk errors, or malware — Windows cannot verify component integrity and refuses to install new updates.

## Common Causes

- **Interrupted Windows updates** — A previous update was partially installed, leaving the component store in an inconsistent state.
- **Disk errors or bad sectors** — Storage corruption damages files in the WinSxS directory.
- **Malware damage** — Malicious software modifying or deleting system files in the component store.
- **Power loss during updates** — A shutdown or power failure mid-update corrupts the servicing stack.

## How to Fix

### Run DISM to Repair the Component Store

DISM (Deployment Image Servicing and Management) is the primary tool for fixing component store corruption.

**Scan for corruption:**

```cmd
DISM /Online /Cleanup-Image /ScanHealth
```

**Restore health using Windows Update as a source:**

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

This process may take 10–15 minutes. Do not interrupt it.

**If DISM fails with network errors**, use a Windows installation media as the repair source:

1. Mount a Windows ISO or insert installation media.
2. Note the drive letter of the mounted media (e.g., `D:`).

```cmd
DISM /Online /Cleanup-Image /RestoreHealth /Source:D:\Sources\install.wim /LimitAccess
```

Replace `D:` with the actual drive letter of your installation media.

### Run SFC After DISM

```cmd
sfc /scannow
```

SFC (System File Checker) verifies and repairs individual system files. Always run it after DISM to ensure all files are consistent.

If SFC reports errors it cannot fix, run DISM again and then SFC a second time:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Reset Windows Update Components

If DISM and SFC don't resolve the issue, fully reset the Windows Update stack:

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
```

Rename the cache folders:

```cmd
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
ren C:\Windows\System32\catroot2 catroot2.old
```

Restart the services:

```cmd
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

Try running Windows Update again.

### Check and Repair Disk Errors

```cmd
chkdsk C: /f /r
```

Press `Y` to schedule for next restart, then reboot. Disk corruption in the WinSxS folder is a common root cause.

**Check disk health:**

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, OperationalStatus
```

### Use the System Update Readiness Tool

For persistent cases, download and run Microsoft's System Update Readiness Tool (CheckSur):

1. Download the appropriate version from Microsoft's support site.
2. Run the installer and let it complete.
3. Restart your computer.
4. Try running Windows Update again.

**View the CBS log for specific corruption details:**

```powershell
Get-Content "C:\Windows\Logs\CBS\CBS.log" -Tail 100
```

### Perform an In-Place Upgrade Repair

If all other methods fail, an in-place upgrade repair reinstalls Windows while keeping your files and apps:

1. Download the Windows Media Creation Tool from [Microsoft's website](https://www.microsoft.com/software-download/).
2. Run the tool and select **Upgrade this PC now**.
3. Choose **Keep personal files and apps**.
4. Complete the installation.

## Examples

This error commonly occurs in these scenarios:

- **After a failed feature update** — Windows 10 to 11 upgrade interrupted by power loss or error.
- **During cumulative updates** — Monthly security updates fail to install repeatedly.
- **After disk cleanup** — Aggressive cleanup tools removing WinSxS files.
- **On systems with aging drives** — Hard drive bad sectors corrupting component store files.

## Related Errors

- [Error 0x800f0922]({{< relref "/os/windows/windows-update-0x800f0922" >}}) — CBS connector disabled, update service issues
- [Error 0x80070002]({{< relref "/os/windows/windows-update-0x80070002" >}}) — File Not Found during Windows Update
- [Error 0x80070005]({{< relref "/os/windows/windows-update-0x80070005" >}}) — Access Denied during Windows Update
- [Error 0x8024402c]({{< relref "/os/windows/windows-update-0x8024402c" >}}) — Windows Update connection error
