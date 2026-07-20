---
title: "[Solution] Windows Update Error 0x80073D13 — Package Dependency Failed Fix"
description: "Fix Windows Update error 0x80073D13 (package dependency failed) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80073D13 — Package Dependency Failed Fix

Windows Update error 0x80073D13 indicates a package dependency has failed. The system cannot install or update a package because a required dependency package is missing, corrupted, or incompatible.

## Description

The full error message reads:

> "Error 0x80073D13: The package dependency operation failed."

This error occurs when Windows tries to resolve package dependencies and finds a missing or corrupted required package. Framework packages and library dependencies are the most common failure points.

## Common Causes

1. **Missing framework packages** — Required .NET or UWP framework packages are absent.
2. **Corrupted dependencies** — Dependency packages are damaged or incomplete.
3. **Version mismatch** — Installed dependency versions incompatible with the target package.
4. **Incomplete framework updates** — Framework packages not fully updated.

## Solutions

### Solution 1: Check and Install Dependencies

```powershell
Get-AppxPackage | Select-Object Name, Version | Sort-Object Name
```

Compare installed framework versions with package requirements.

### Solution 2: Run DISM to Repair

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

This will attempt to restore missing and corrupted package dependencies.

### Solution 3: Try Manual Package Install

Download the package and its dependencies from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install them individually.

### Solution 4: Reset Store and Retry

```cmd
wsreset.exe
```

Then retry the installation through the Microsoft Store.

## Related Errors

- [Error 0x80073CF6]({{< relref "/os/windows/windows-update-0x80073cf6" >}}) — Package install failed
- [Error 0x80073D12]({{< relref "/os/windows/windows-update-0x80073d12" >}}) — Package repository corrupt
- [Error 0x80073701]({{< relref "/os/windows/windows-update-0x80073701" >}}) — Required package missing
