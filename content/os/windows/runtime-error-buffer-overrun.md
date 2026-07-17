---
title: "[Solution] Buffer Overrun Runtime Error — Stack Buffer Overflow"
description: "Fix buffer overrun runtime errors on Windows. Resolve stack buffer overflow crashes, stack protection failures, and /GS violations."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["buffer-overrun", "stack-overflow", "security", "gs", "stack-cookie", "memory"]
weight: 5
---

# Buffer Overrun Runtime Error — Stack Buffer Overflow

A buffer overrun runtime error occurs when a program writes data beyond the boundary of a stack-allocated buffer, triggering the `/GS` stack cookie protection. The error message reads:

> "Runtime Error! Program: C:\...\program.exe
> This application has requested the Runtime to terminate it in an unusual way."

Or in a crash dialog:

> "Stack buffer overrun — The stack cookie was corrupted."

## What This Error Means

Buffer overruns (stack buffer overflows) happen when a function writes more data to a stack buffer than it was allocated. Windows includes `/GS` stack protection that places a "cookie" value between the buffer and the return address. When a buffer overrun corrupts this cookie, the program is terminated to prevent exploitation. This is a security mitigation, not a Windows bug.

## Common Causes

- Application bug writing past buffer boundaries (most common)
- Unbounded `strcpy`, `sprintf`, or `gets` calls in legacy code
- Malicious input designed to trigger a buffer overflow exploit
- Fuzzing or testing with oversized inputs
- Third-party library with a buffer overflow vulnerability

## How to Fix

### Update the Application

Buffer overrun terminations are application bugs. Check for updates from the software vendor:

```powershell
# Check installed version
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*AppName*" } | Select-Object Name, Version
```

### Check for Patches

Visit the vendor's website or use the application's built-in update mechanism. Security patches often fix buffer overrun vulnerabilities.

### Enable Enhanced /GS Protection

Ensure the application is compiled with full `/GS` protection:

```cmd
# Check if the binary has /GS enabled (requires dumpbin from Visual Studio)
dumpbin /headers "C:\Path\To\app.exe" | findstr /GS
```

### Run Windows Defender Exploit Guard

```powershell
# Enable Exploit Guard
Set-ProcessMitigation -Name "app.exe" -Enable EnableStackProtection, EnableDynamicCode
```

### Disable and Re-enable DEP

```cmd
# Check DEP status
wmic OS get DataExecutionPrevention_SupportPolicy

# Add application to DEP exception list (if it legitimately needs it)
# System Properties > Advanced > Performance Settings > DEP
```

## Related Errors

- [Stack Overflow Runtime Error]({{< relref "/os/windows/runtime-error-stack-overflow" >}}) — Stack overflow from deep recursion
- [Access Violation 0xC0000005]({{< relref "/os/windows/runtime-error-c0000005" >}}) — General memory access violations
- [Unhandled Exception]({{< relref "/os/windows/runtime-error-unhandled-exception" >}}) — Unhandled exceptions at crash address
