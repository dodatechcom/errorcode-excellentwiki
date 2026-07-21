---
title: "[Solution] Event ID 6008 Previous System Shutdown Unclean Fix"
description: "Fix Windows Event ID 6008 indicating the previous system shutdown was unexpected. Resolve unclean shutdown errors and prevent data loss on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Event ID 6008 Previous System Shutdown Unclean Fix

Event ID 6008 in the System log means Windows detected that the previous shutdown was not clean. The system lost power unexpectedly or crashed before it could complete a proper shutdown sequence.

## Common Causes
- Power outage or sudden power loss
- BSOD crash that prevented clean shutdown
- Hardware power button pressed for force shutdown
- UPS battery depleted causing abrupt power cut
- Faulty power supply causing intermittent power loss

## How to Fix

### Solution 1: Check Power Supply

Test the power supply with a PSU tester or replace it if the system shuts down unexpectedly without a BSOD.

### Solution 2: Review Crash Details

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=6008} -MaxEvents 5 | Format-Table TimeCreated, Message
```

### Solution 3: Enable UPS Monitoring

Connect a UPS and install its monitoring software to allow Windows to shut down gracefully during power events.

### Solution 4: Check Event Logs Before the Crash

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Level=1,2; StartTime=(Get-Date).AddDays(-7)} | Format-Table TimeCreated, Id, Message -Wrap
```

### Solution 5: Check Disk and Memory

```cmd
chkdsk C: /f /r
mdsched.exe
```

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=6008} -MaxEvents 10
```
