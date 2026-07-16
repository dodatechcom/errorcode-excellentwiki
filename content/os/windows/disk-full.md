---
title: "[Solution] There Is Not Enough Space on the Disk Fix"
description: "Fix 'There is not enough space on the disk' error on Windows 10 and 11. Free up disk space, extend partitions, clear temporary files, and manage storage."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["disk-full", "storage", "low-disk-space", "temp-files", "cleanup"]
weight: 5
---

# [Solution] There Is Not Enough Space on the Disk Fix

This error occurs when Windows or an application tries to write data to a disk but there isn't enough free space to complete the operation. It can appear during file operations, software installations, Windows Updates, or when the system drive runs critically low on space.

This error affects both Windows 10 and 11 and can range from a simple nuisance (a few MB short) to a critical system issue (system drive completely full, preventing Windows from functioning).

## Description

The full error message typically reads:

> "There is not enough space on [drive letter]. You need an additional [amount] to copy these files."

Or:

> "Disk is full. Free up space on this drive."

When the system drive (usually C:) runs out of space, Windows cannot create page files, write temporary data, install updates, or even function properly. This can lead to application crashes, system instability, and data loss.

## Common Causes

- **Full Downloads or temp folders** — Accumulated temporary files, browser caches, and download leftovers consuming disk space.
- **Windows Update cache** — Old update files consuming several GB in the SoftwareDistribution folder.
- **Large applications or games** — Modern games and applications requiring 50–100+ GB of storage.
- **System restore points and hibernation files** — Hidden system files consuming significant space.

## How to Fix

### Run Disk Cleanup

Windows includes a built-in tool for clearing temporary and system files:

```cmd
cleanmgr /d C:
```

Or use the more comprehensive system cleanup:

```cmd
cleanmgr /d C: /sageset:1
```

Select all categories to clean, then run:

```cmd
cleanmgr /d C: /sagerun:1
```

**Use Storage Sense (Windows 10/11):**

1. Press `Win + I` to open **Settings**.
2. Go to **System > Storage**.
3. Enable **Storage Sense**.
4. Click **Configure Storage Sense or run it now**.
5. Set it to run weekly or monthly.
6. Enable **Delete temporary files that my apps aren't using**.

### Clear Windows Update Cache

```cmd
net stop wuauserv
net stop bits
rd /s /q C:\Windows\SoftwareDistribution\Download
net start wuauserv
net start bits
```

### Clear Temporary Files Manually

```powershell
# Clear user temp folder
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue

# Clear Windows temp folder
Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue

# Clear Windows Installer patches (old ones)
Remove-Item -Path "C:\Windows\Installer\$PatchCache$" -Recurse -Force -ErrorAction SilentlyContinue
```

### Clear Browser Caches

Browser caches can consume several GB:

```powershell
# Chrome
Remove-Item -Path "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Cache\*" -Recurse -Force -ErrorAction SilentlyContinue

# Edge
Remove-Item -Path "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Cache\*" -Recurse -Force -ErrorAction SilentlyContinue

# Firefox
Remove-Item -Path "$env:LOCALAPPDATA\Mozilla\Firefox\Profiles\*\cache2\*" -Recurse -Force -ErrorAction SilentlyContinue
```

### Disable Hibernation to Free Space

Hibernation allocates space equal to your RAM:

```cmd
powercfg -h off
```

On a system with 16 GB RAM, this frees approximately 16 GB.

### Extend the Partition

If the disk has unallocated space adjacent to the system partition:

```powershell
Get-Partition | Select-Object DiskNumber, PartitionNumber, DriveLetter, Size, Type | Format-Table -AutoSize
```

Use Disk Management to extend the volume:
1. Press `Win + X` and select **Disk Management**.
2. Right-click the C: drive partition.
3. Select **Extend Volume**.
4. Follow the wizard to use available unallocated space.

### Find Large Files

Identify what's consuming disk space:

```powershell
Get-ChildItem -Path C:\ -Recurse -File -ErrorAction SilentlyContinue |
    Sort-Object Length -Descending |
    Select-Object -First 20 FullName, @{N="SizeMB";E={[math]::Round($_.Length/1MB,2)}} |
    Format-Table -AutoSize
```

### Remove Old Windows Installations

After a feature update, the old installation is kept in `Windows.Old`:

```cmd
rd /s /q C:\Windows.old
```

Or use Disk Cleanup's **Clean up system files** option to remove it safely.

## Examples

This error commonly occurs in these scenarios:

- **Before Windows updates** — Cumulative updates require several GB of free space to download and install.
- **During application installation** — Large games or creative software need more space than available.
- **With small SSDs** — 128 GB or 256 GB drives filling up quickly with modern software.
- **After large downloads** — Downloaded ISOs, installers, and media files accumulating over time.

## Related Errors

- [Access Violation 0xC0000005]({{< relref "/os/windows/runtime-error-c0000005" >}}) — Memory errors from insufficient disk space for page files
- [Windows Update 0x80070002]({{< relref "/os/windows/windows-update-0x80070002" >}}) — File Not Found errors from incomplete downloads
- [Application Error Event ID 1000]({{< relref "/os/windows/event-1000" >}}) — Application crashes from disk write failures
