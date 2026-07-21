---
title: "[Solution] Windows Defender Scan Stuck Pending Fix"
description: "Fix Windows Defender scan that is stuck in pending state and not completing on Windows. Resolve Defender quick scan and full scan hangs."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Defender Scan Stuck Pending Fix

A Windows Defender scan stuck in pending state will not progress beyond its current percentage. This prevents malware scanning from completing.

## Common Causes
- Large number of files causing slow scan progress
- File in a locked state causing the scan to hang
- Defender service consuming excessive CPU or memory
- Corrupted Defender definition database
- Scheduled scan conflicting with manual scan

## How to Fix

### Solution 1: Restart Windows Defender Service

```powershell
Restart-Service -Name WinDefend -Force
```

### Solution 2: Cancel and Rescan

```powershell
Stop-Process -Name MsMpEng -Force -ErrorAction SilentlyContinue
Start-MpScan -ScanType QuickScan
```

### Solution 3: Update Definitions

```powershell
Update-MpSignature
```

### Solution 4: Clear Defender Cache

```cmd
del /q /s C:\ProgramData\Microsoft\Windows Defender\Support\*
del /q /s C:\ProgramData\Microsoft\Windows Defender\Scans\History\*
```

### Solution 5: Run Offline Scan

```powershell
Start-MpScan -ScanType OfflineScan
```

## Examples
```powershell
Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled, QuickScanEndTime, FullScanEndTime, AntivirusSignatureLastUpdated
```
