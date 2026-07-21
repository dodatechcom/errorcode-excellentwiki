---
title: "[Solution] BSOD 0x0000007e EXCEPTION_NOT_HANDLED Fix"
description: "Fix Blue Screen error 0x0000007e SYSTEM_THREAD_EXCEPTION_NOT_HANDLED on Windows. Resolve unhandled system thread exception and driver crash errors."
platforms: ["windows"]
severities: ["error"]
error_types: ["bsod"]
weight: 10
---

# [Solution] BSOD 0x0000007e EXCEPTION_NOT_HANDLED Fix

Stop code 0x0000007e is a generic SYSTEM_THREAD_EXCEPTION_NOT_HANDLED error where a system thread generated an exception that the error handler did not catch. The specific failing module is identified in the blue screen details.

## Common Causes
- Driver bug causing an unhandled exception in kernel mode
- Incompatible driver version with current Windows build
- Corrupted system files from disk errors or failed updates
- Third-party security software kernel driver failure
- Hardware failure generating invalid kernel exceptions

## How to Fix

### Solution 1: Identify the Failing Module

Check the blue screen for the failing module name (for example nvlddmkm.sys or igdkmd64.sys).

### Solution 2: Update the Identified Driver

Download the latest driver for the specific module from the manufacturer website.

### Solution 3: Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Solution 4: Boot in Last Known Good Configuration

Restart and press F8 or Shift+Restart to access Advanced Boot Options and select Last Known Good Configuration.

### Solution 5: Enable Driver Verifier

```cmd
verifier /standard /all
```

Use verifier to catch the driver causing the exception before the crash occurs.

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Level=1; Id=1001} -MaxEvents 3 | Select-Object TimeCreated, Message
```
