---
title: "[Solution] Windows Update Error 0x8007000E — Out of Memory Fix"
description: "Fix Windows Update error 0x8007000E (out of memory) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x8007000E — Out of Memory Fix

Windows Update error 0x8007000E indicates the system ran out of memory during an update operation. This typically means the page file is too small or too many programs are consuming available RAM.

## Description

The full error message reads:

> "There were problems downloading some updates, but we'll try again later. Error 0x8007000E"

Error 0x8007000E maps to `ERROR_OUTOFMEMORY`, meaning Windows Update cannot allocate enough memory to complete the operation. This can happen even on systems with plenty of RAM if the page file is misconfigured.

## Common Causes

1. **Insufficient page file size** — Virtual memory not configured adequately for update operations.
2. **Too many background programs** — Applications consuming excessive RAM.
3. **Corrupted update cache** — Damaged cache files consuming extra memory.
4. **Faulty RAM** — Hardware issues causing memory allocation failures.

## Solutions

### Solution 1: Increase Virtual Memory

Open System Properties (`sysdm.cpl`) > **Advanced** > **Performance Settings** > **Advanced** > **Virtual Memory** > **Change**.

Uncheck **Automatically manage** and set:

- Initial size: **4096 MB**
- Maximum size: **8192 MB**

Or use PowerShell:

```powershell
$cs = Get-WmiObject Win32_ComputerSystem
$cs.AutomaticManagedPagefile = $false
$cs.Put()
$pf = Get-WmiObject Win32_PageFileSetting
$pf.InitialSize = 4096
$pf.MaximumSize = 8192
$pf.Put()
```

Restart your computer after changing.

### Solution 2: Close Memory-Heavy Programs

```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name, @{N='MB';E={[math]::Round($_.WorkingSet64/1MB)}}
```

Close unnecessary applications, especially browsers with many tabs, video editors, and virtual machines.

### Solution 3: Try Manual Update Download

Download the update manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it offline.

### Solution 4: Run Windows Update Troubleshooter

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Click **Run** next to **Windows Update**.

## Related Errors

- [Error 0x80070008]({{< relref "/os/windows/windows-update-0x80070008" >}}) — Not enough memory variant
- [Error 0x80070002]({{< relref "/os/windows/windows-update-0x80070002" >}}) — File Not Found
- [Error 0x80070005]({{< relref "/os/windows/windows-update-0x80070005" >}}) — Access Denied
