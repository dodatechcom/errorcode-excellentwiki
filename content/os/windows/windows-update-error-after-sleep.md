---
title: "[Solution] Windows Update Fails After Sleep Fix"
description: "Fix Windows Update that fails to download or install updates after the computer resumes from sleep or hibernation on Windows 10/11."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Update Fails After Sleep Fix

Windows Update may fail after the computer wakes from sleep or hibernation because the update service has lost its connection state or cached data has become stale during the low-power state.

## Common Causes
- Network adapter power management disconnecting during sleep
- Windows Update service not properly resuming after wake
- Cached update data corrupted during low-power transition
- BITS job stuck in an error state after wake
- Time sync issues after waking from extended sleep

## How to Fix

### Solution 1: Reset Windows Update Services

```cmd
net stop wuauserv
net stop bits
net start wuauserv
net start bits
```

### Solution 2: Disable Network Adapter Power Management

1. Open Device Manager
2. Expand Network adapters
3. Right-click your adapter > Properties > Power Management
4. Uncheck Allow the computer to turn off this device to save power

### Solution 3: Clear BITS Queue

```cmd
bitsadmin /reset /allusers
```

### Solution 4: Schedule Updates for Active Hours

Go to Settings > Windows Update > Advanced options and set active hours to prevent updates during sleep periods.

### Solution 5: Run Update Troubleshooter

Go to Settings > System > Troubleshoot and run the Windows Update troubleshooter.

## Examples
```powershell
bitsadmin /list /allusers
```
