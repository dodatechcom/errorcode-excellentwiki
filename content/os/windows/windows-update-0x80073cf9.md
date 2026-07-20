---
title: "[Solution] Windows Update Error 0x80073CF9 — Package Install Failed Variant Fix"
description: "Fix Windows Update error 0x80073CF9 (package could not be installed) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80073CF9 — Package Could Not Be Installed Fix

Windows Update error 0x80073CF9 is a variant of the package installation failure error. It occurs when the system cannot install an app package due to disk space issues, corrupted components, or service conflicts.

## Description

The full error message reads:

> "Error 0x80073CF9: The package could not be installed because a Windows Defender filter prevents the install."

Or alternatively:

> "Error 0x80073CF9: Service registration is missing or corrupt."

This error differs from 0x80073CF6 in that it typically involves disk space constraints or the Windows Defender App Installer filter blocking the installation.

## Common Causes

1. **Insufficient disk space** — Not enough space to extract and install the package.
2. **Corrupted servicing stack** — The AppX deployment service is damaged.
3. **Defender filter conflict** — Windows Defender blocking the installation.
4. **Corrupted temporary files** — Damaged staging files for package installation.

## Solutions

### Solution 1: Check Disk Space

```powershell
Get-PSDrive C | Select-Object Used, Free, @{N='FreeGB';E={[math]::Round($_.Free/1GB,2)}}
```

Ensure at least 5 GB free on the system drive. Free space using Disk Cleanup:

```cmd
cleanmgr /d C:
```

### Solution 2: Run DISM to Repair

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

### Solution 3: Try Clean Boot

1. Press `Win + R`, type `msconfig`, press Enter.
2. Go to **Services** tab, check **Hide all Microsoft services**, click **Disable all**.
3. Go to **Startup** tab, click **Open Task Manager**, disable all startup items.
4. Restart and try the installation.

### Solution 4: Clear Package Staging Files

```cmd
del /q/f/s C:\Windows\SoftwareDistribution\Download\*
net stop wuauserv
net start wuauserv
```

## Related Errors

- [Error 0x80073CF6]({{< relref "/os/windows/windows-update-0x80073cf6" >}}) — Package install failed
- [Error 0x80073D05]({{< relref "/os/windows/windows-update-0x80073d05" >}}) — Package store operation failed
- [Error 0x80070070]({{< relref "/os/windows/windows-update-0x80070070" >}}) — Insufficient disk space
