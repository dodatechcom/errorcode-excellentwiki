---
title: "[Solution] Windows Update Error 0x80070003 Path Not Found Fix"
description: "Fix Windows Update error 0x80070003 (path not found) on Windows 10 and 11. Resolve missing update file paths with cache resets and folder repairs."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
tags: ["windows-update", "0x80070003", "path-not-found", "file-missing"]
weight: 5
---

# [Solution] Windows Update Error 0x80070003 Path Not Found Fix

Error 0x80070003 means Windows Update cannot find a required file or path during the update process. The update agent expects certain files or directories to exist and cannot proceed when they are missing.

This error is similar to 0x80070002 but specifically indicates a path-not-found condition, often caused by corrupted SoftwareDistribution folders or incomplete previous updates.

## What This Error Means

The full error message typically reads:

> "Some updates were not installed. Errors found: Code 0x80070003. Windows Update ran into a problem."

Error 0x80070003 maps to `ERROR_PATH_NOT_FOUND` — the specified path does not exist. Common triggers include:

- **Corrupted SoftwareDistribution folder** — Update cache has invalid entries
- **Incomplete previous update** — A prior update left the system in an inconsistent state
- **Missing catroot2 folder** — Catalog database folder is missing or damaged
- **Registry issues** — Update-related registry entries pointing to nonexistent paths

## Common Causes

1. **Corrupted SoftwareDistribution folder** — Damaged update cache.
2. **Incomplete previous update** — Interrupted update left inconsistent state.
3. **Missing catroot2 folder** — Catalog database folder missing.
4. **Registry issues** — Update registry entries pointing to wrong paths.

## How to Fix

### Reset Windows Update Cache

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
rd /s /q "C:\Windows\SoftwareDistribution"
rd /s /q "C:\Windows\System32\catroot2"
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

### Create Missing Directories

If the directories were deleted and not recreated:

```cmd
mkdir "C:\Windows\SoftwareDistribution"
mkdir "C:\Windows\System32\catroot2"
```

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check for Registry Issues

The update path references are stored in the registry. Reset them:

```cmd
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate" /v LastRestorePointSetAttempt /f
```

### Run Windows Update Troubleshooter

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter.
3. Apply any fixes it suggests.

### Download and Install Manually

1. Note the KB number from Windows Update.
2. Visit [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Download and install the update manually.

## Related Errors

- [Error 0x80070002]({{< relref "/os/windows/windows-update-0x80070002" >}}) — File Not Found (similar but different cause)
- [Error 0x80070005]({{< relref "/os/windows/windows-update-0x80070005" >}}) — Access Denied during update
- [Error 0x80073712]({{< relref "/os/windows/windows-update-0x80073712" >}}) — Component store corrupted
