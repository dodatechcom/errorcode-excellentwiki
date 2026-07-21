---
title: "[Solution] Windows Update Disconnecting During Download Fix"
description: "Fix Windows Update that keeps disconnecting from the network during update download on Windows 10 and 11. Resolve intermittent download failures."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Update Disconnecting During Download Fix

Windows Update loses its network connection while downloading updates, causing the download to fail and restart. This creates a loop where updates never complete downloading.

## Common Causes
- Wi-Fi adapter power management disconnecting during idle
- Network adapter driver issue causing intermittent drops
- BITS (Background Intelligent Transfer Service) throttling
- Third-party software interfering with BITS
- Router or modem connection instability

## How to Fix

### Solution 1: Disable Wi-Fi Power Management

1. Open Device Manager
2. Expand Network adapters
3. Right-click your Wi-Fi adapter > Properties > Power Management
4. Uncheck Allow the computer to turn off this device to save power

### Solution 2: Reset BITS

```cmd
net stop bits
bitsadmin /reset /allusers
net start bits
```

### Solution 3: Use Ethernet Connection

Switch to a wired Ethernet connection for more reliable update downloads.

### Solution 4: Configure BITS Priority

```powershell
Set-BitsTransfer -BitsJob $job -Priority High
```

### Solution 5: Download Update Manually

Download the update package from the Microsoft Update Catalog and install offline.

## Examples
```powershell
Get-BitsTransfer | Select-Object JobId, DisplayName, JobState, BytesTransferred, BytesTotal
```
