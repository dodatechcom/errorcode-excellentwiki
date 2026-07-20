---
title: "[Solution] Windows Update Error 0x80070008 — Not Enough Memory Fix"
description: "Fix Windows Update error 0x80070008 (not enough memory) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80070008 — Not Enough Memory Fix

Windows Update error 0x80070008 indicates the system ran out of memory during an update. This is similar to 0x8007000E but typically occurs when the page file cannot expand or is corrupted.

## Description

The full error message reads:

> "There were problems downloading some updates, but we'll try again later. Error 0x80070008"

Error 0x80070008 maps to `ERROR_NOT_ENOUGH_MEMORY`, a memory allocation failure that prevents Windows Update from completing its operations. The system may have physical RAM available but cannot allocate virtual memory properly.

## Common Causes

1. **Page file too small or corrupted** — Virtual memory insufficient for update operations.
2. **Too many background applications** — Programs consuming available memory.
3. **Corrupted Windows Update cache** — Damaged cache forcing excessive memory use.
4. **Malfunctioning RAM** — Faulty memory modules causing allocation failures.

## Solutions

### Solution 1: Reset Page File

```cmd
wmic computersystem set AutomaticManagedPagefile=False
wmic pagefileset set InitialSize=4096
wmic pagefileset set MaximumSize=8192
```

Restart your computer for changes to take effect.

### Solution 2: Close Background Programs

```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 15 Name, @{N='MB';E={[math]::Round($_.WorkingSet64/1MB)}}
```

End unnecessary processes using Task Manager or:

```cmd
taskkill /F /IM chrome.exe
taskkill /F /IM firefox.exe
```

### Solution 3: Run Windows Update Troubleshooter

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Click **Run** next to **Windows Update**.

### Solution 4: Reset Windows Update Components

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
ren C:\Windows\System32\catroot2 catroot2.old
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

## Related Errors

- [Error 0x8007000E]({{< relref "/os/windows/windows-update-0x8007000e" >}}) — Out of memory
- [Error 0x80070070]({{< relref "/os/windows/windows-update-0x80070070" >}}) — Insufficient disk space
- [Error 0x80070002]({{< relref "/os/windows/windows-update-0x80070002" >}}) — File Not Found
