---
title: "[Solution] NTSTATUS STATUS_NOT_SUPPORTED Fix"
description: "Fix NTSTATUS STATUS_NOT_SUPPORTED error on Windows when an operation or feature is not supported by the system or component."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] NTSTATUS STATUS_NOT_SUPPORTED Fix

The NTSTATUS STATUS_NOT_SUPPORTED (0xC00000BB) error means the requested operation is not supported by the target system, driver, or component. This commonly occurs with older hardware, legacy applications, or incompatible protocol versions.

## Common Causes
- Hardware does not support the requested feature or command
- Outdated driver lacking support for newer API calls
- Network protocol version mismatch between client and server
- BIOS or firmware not supporting a requested capability
- Application attempting an unsupported operation on the OS version

## How to Fix

### Solution 1: Check Hardware Compatibility

Verify your hardware supports the feature you are trying to use by checking the manufacturer specifications.

### Solution 2: Update BIOS and Firmware

Download and install the latest BIOS and firmware updates from your hardware manufacturer.

### Solution 3: Update Device Drivers

```powershell
pnputil /scan-devices
```

Let Windows scan for and install updated drivers.

### Solution 4: Verify Protocol Compatibility

```powershell
Get-SmbConnection | Select-Object ServerName, Dialect
```

### Solution 5: Check Windows Feature Support

```powershell
Get-WindowsOptionalFeature -Online | Where-Object { $_.State -eq 'Enabled' } | Select-Object FeatureName
```

Enable any required Windows features that may be disabled.

## Examples
```powershell
Get-SmbConnection | Select-Object ServerName, ShareName, Dialect, Status
```
