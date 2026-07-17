---
title: "[Solution] Windows Update Error 0x80240017 Not Applicable Fix"
description: "Fix Windows Update error 0x80240017 (not applicable to this computer) on Windows 10 and 11. Resolve update compatibility issues with WSUS, product matching, and manual installs."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
tags: ["windows-update", "0x80240017", "not-applicable", "compatibility", "wsus"]
weight: 5
---

# [Solution] Windows Update Error 0x80240017 Not Applicable Fix

Error 0x80240017 means the update is "not applicable" to your computer. Windows Update determined that the update does not match your system configuration, operating system version, or hardware architecture.

This error commonly occurs in enterprise environments with WSUS servers, when downloading updates manually, or when there is a mismatch between the update and your Windows version.

## What This Error Means

The full error message typically reads:

> "Some updates were not installed. Errors found: Code 0x80240017. Windows Update ran into a problem."

Or:

> "Not applicable. The update does not apply to or is not compatible with this computer."

Error 0x80240017 maps to `WU_E_NOT_APPLICABLE` — the update package is valid but does not apply to the current system. This can be caused by:

- **Wrong update architecture** — Trying to install a 32-bit update on a 64-bit system
- **Wrong Windows version** — Update designed for a different Windows build
- **WSUS configuration issues** — Enterprise WSUS not targeting the correct product
- **Corrupted Windows Update components** — Update agent cannot determine applicability

## Common Causes

1. **Wrong update architecture** — Attempting to install a 32-bit update on a 64-bit system.
2. **Windows version mismatch** — The update is designed for a different Windows build.
3. **WSUS server misconfiguration** — Enterprise update server not targeting the correct product.
4. **Corrupted Windows Update components** — Update agent cannot determine applicability.

## How to Fix

### Verify Your Windows Version and Architecture

```cmd
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
```

Ensure the update matches your system:
- **x64** systems need 64-bit updates
- **ARM64** systems need ARM64 updates
- Verify the update targets your specific Windows build

### Check Installed Updates

```powershell
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10 HotFixID, Description, InstalledOn | Format-Table -AutoSize
```

The update may already be installed or superseded by a newer update.

### Reset Windows Update Components

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

### Download and Install Manually

1. Note the KB number from Windows Update.
2. Visit [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Search for the KB number.
4. Download the correct version for your architecture.
5. Run the installer manually.

### Check WSUS Configuration (Enterprise)

If your organization uses WSUS:

1. Open the **WSUS Administration Console**.
2. Navigate to **Updates** and find the update.
3. Verify the update is **approved** for the correct computer group.
4. Check that the update targets the correct product and Windows version.
5. Run `wuauclt /detectnow` on the client to recheck.

### Run Windows Update Troubleshooter

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter.
3. Apply any fixes it suggests.

## Related Errors

- [Error 0x800f0922]({{< relref "/os/windows/windows-update-0x800f0922" >}}) — CBS connector disabled
- [Error 0x80070002]({{< relref "/os/windows/windows-update-0x80070002" >}}) — File Not Found during update
- [Error 0x80070005]({{< relref "/os/windows/windows-update-0x80070005" >}}) — Access Denied during update
