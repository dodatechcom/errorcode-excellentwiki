---
title: "[Solution] Windows Update Error 0x80073D22 — Package Resource Limit Fix"
description: "Fix Windows Update error 0x80073D22 (package resource limit) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80073D22 — Package Resource Limit Fix

Windows Update error 0x80073D22 indicates the system has hit a package resource limit. This typically means too many Store apps are running or updating simultaneously, or the system has exhausted resources for package operations.

## Description

The full error message reads:

> "Error 0x80073D22: The package deployment operation could not be completed because of a resource limit."

This error occurs when Windows cannot allocate sufficient resources for package installation due to concurrent operations, low disk space, or memory constraints.

## Common Causes

1. **Too many concurrent Store operations** — Multiple apps updating simultaneously.
2. **Insufficient disk space** — Not enough space for package extraction.
3. **Memory pressure** — System running low on available RAM.
4. **Background processes** — Other applications consuming package-related resources.

## Solutions

### Solution 1: Free Disk Space

```cmd
cleanmgr /d C:
```

Ensure at least 5 GB free on the system drive.

### Solution 2: Close Other Applications

```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name, @{N='MB';E={[math]::Round($_.WorkingSet64/1MB)}}
```

Close unnecessary applications and browser tabs.

### Solution 3: Try Again Later

Wait 10–15 minutes and retry. The resource contention may resolve itself as background processes complete.

### Solution 4: Restart Your Computer

A fresh boot clears memory and stops background processes that may be holding resources:

```cmd
shutdown /r /t 0
```

## Related Errors

- [Error 0x80073D1A]({{< relref "/os/windows/windows-update-0x80073d1a" >}}) — Package download failed
- [Error 0x8007000E]({{< relref "/os/windows/windows-update-0x8007000e" >}}) — Out of memory
- [Error 0x80070070]({{< relref "/os/windows/windows-update-0x80070070" >}}) — Insufficient disk space
