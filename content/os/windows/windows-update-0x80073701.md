---
title: "[Solution] Windows Update Error 0x80073701 — Required Package Missing Fix"
description: "Fix Windows Update error 0x80073701 (required package missing) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80073701 — Required Package Missing Fix

Windows Update error 0x80073701 indicates a required package is missing from the system. Windows cannot complete the update because a prerequisite package that other updates depend on has been removed or corrupted.

## Description

The full error message reads:

> "There were problems installing some updates, but we'll try again later. Error 0x80073701"

Error 0x80073701 maps to `ERROR_SXS_ASSEMBLY_MISSING`, meaning a required system assembly (package) is missing from the component store. Cumulative and feature updates often fail because a base servicing package is absent.

## Common Causes

1. **Missing servicing stack update** — A required servicing stack update was not installed or was removed.
2. **Corrupted component store** — Damaged WinSxS files causing package resolution failures.
3. **Aggressive disk cleanup** — Cleanup tools removing required system packages.
4. **Failed previous update** — An update that provided the required package did not complete.

## Solutions

### Solution 1: Install Missing Servicing Stack Update

Download and install the latest Servicing Stack Update (SSU) for your Windows version from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).

### Solution 2: Run DISM to Repair

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

This will attempt to download and restore missing packages using Windows Update as a source.

### Solution 3: Run System File Checker

```cmd
sfc /scannow
```

After SFC completes, run DISM again if errors were found:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Solution 4: Try Manual Update Installation

Download the update manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it using:

```cmd
wusa.exe C:\path\to\update.msu /quiet /norestart
```

## Related Errors

- [Error 0x80073712]({{< relref "/os/windows/windows-update-0x80073712" >}}) — Component store corrupted
- [Error 0x800f0922]({{< relref "/os/windows/windows-update-0x800f0922" >}}) — CBS connector disabled
- [Error 0x80070002]({{< relref "/os/windows/windows-update-0x80070002" >}}) — File Not Found
