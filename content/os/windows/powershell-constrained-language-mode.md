---
title: "[Solution] PowerShell Constrained Language Mode Error Fix"
description: "Fix PowerShell constrained language mode restriction preventing script execution. Resolve AppLocker and WDAC language mode blocks on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] PowerShell Constrained Language Mode Error Fix

PowerShell runs in Constrained Language Mode when AppLocker or Windows Defender Application Control (WDAC) policies restrict script execution.

## Common Causes
- AppLocker policy enforcing constrained language mode
- WDAC (Device Guard) policy restricting script execution
- System Center Configuration Manager enforcing WDAC
- Enterprise GPO deploying application control policies
- Windows Defender Application Guard activating restricted mode

## How to Fix

### Solution 1: Check Current Language Mode

```powershell
$ExecutionContext.SessionState.LanguageMode
```

### Solution 2: Review AppLocker Policy

```powershell
Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections
```

### Solution 3: Check WDAC Policy

```powershell
Get-CimInstance -Namespace root\Microsoft\Windows\CI -ClassName MSFT_WDACSIPolicy
```

### Solution 4: Use System Context

Run PowerShell as SYSTEM using PsExec to bypass user-level restrictions:

```cmd
psexec -i -s powershell.exe
```

### Solution 5: Modify AppLocker Rules

Add PowerShell scripts to the allowed list in AppLocker policy through Group Policy.

## Examples
```powershell
$ExecutionContext.SessionState.LanguageMode
Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections
```
