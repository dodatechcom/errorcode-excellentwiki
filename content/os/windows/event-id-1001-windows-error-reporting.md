---
title: "[Solution] Event ID 1001 Windows Error Reporting Fix"
description: "Fix Event ID 1001 Windows Error Reporting events in Application log. Analyze application crash reports and resolve recurring software failures."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] Event ID 1001 Windows Error Reporting Fix

Event ID 1001 in the Application log contains Windows Error Reporting (WER) data when applications crash or encounter errors.

## Common Causes
- Application crash generating a dump file
- .NET Framework runtime error with faulting assembly
- Windows component crashing during update or repair
- Application compatibility issue with Windows version
- Hardware-related errors causing application failures

## How to Fix

### Solution 1: Analyze WER Event Details

```powershell
Get-WinEvent -FilterHashtable @{LogName='Application'; Id=1001} -MaxEvents 10 | ForEach-Object { [xml]$_.ToXml() } | Select-Object -ExpandProperty EventData
```

### Solution 2: Check Fault Bucket Data

The WER event contains a fault bucket ID. Search Microsoft Support with this bucket ID for known issues.

### Solution 3: Disable WER for Specific Application

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" /v DumpFolder /t REG_SZ /d C:\Dumps /f
```

### Solution 4: Install Application Updates

Check the faulting application vendor site for updates that address the specific crash.

### Solution 5: Enable Crash Dumps

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" /v DumpType /t REG_DWORD /d 2 /f
```

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='Application'; Id=1001} -MaxEvents 5 | ForEach-Object { [xml]$_.ToXml() } | Select-Object -ExpandProperty EventData
```
