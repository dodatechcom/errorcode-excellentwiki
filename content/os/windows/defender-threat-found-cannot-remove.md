---
title: "[Solution] Windows Defender Threat Found Cannot Remove Fix"
description: "Fix Windows Defender that detects a threat but cannot remove or quarantine it on Windows. Resolve stuck malware detections and removal failures."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Defender Threat Found Cannot Remove Fix

Windows Defender detects a threat but fails to remove, quarantine, or restore it. The threat remains listed in protection history and the system may be at risk.

## Common Causes
- Malware running in memory preventing file deletion
- Threat embedded in a protected system file
- Defender lacking full access to the threat file location
- Quarantine database corruption
- Rootkit or bootkit preventing removal

## How to Fix

### Solution 1: Run Full Scan

```powershell
Start-MpScan -ScanType FullScan
```

### Solution 2: Use Windows Defender Offline

```powershell
Start-MpScan -ScanType OfflineScan
```

This scans before Windows fully loads, preventing active malware from blocking removal.

### Solution 3: Boot into Safe Mode

Restart in Safe Mode to prevent the threat from running. Then run a full scan from Safe Mode.

### Solution 4: Check Defender Quarantine

```powershell
Get-MpThreatDetection | Select-Object ThreatID, DomainUser, ProcessName, InitialDetectionTime
```

### Solution 5: Reset Defender Definitions

```powershell
Update-MpSignature -Force
```

## Examples
```powershell
Get-MpThreat | Select-Object ThreatID, ThreatName, IsActive
Get-MpThreatDetection | Select-Object ThreatID, InitialDetectionTime
```
