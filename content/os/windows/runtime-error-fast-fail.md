---
title: "[Solution] FastFail Error in Windows — STATUS_STACK_BUFFER_OVERRUN"
description: "Fix fast-fail (fastfail) termination errors on Windows 10/11. Resolve STATUS_STACK_BUFFER_OVERRUN and other fast-fail security terminations."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["fastfail", "fast-fail", "0xC0000409", "stack-buffer-overrun", "security", "gs"]
weight: 5
---

# FastFail Error in Windows — STATUS_STACK_BUFFER_OVERRUN

A fast-fail error occurs when Windows terminates a process immediately due to a detected security violation. The crash shows:

> "Exception code: 0xC0000409 — STATUS_STACK_BUFFER_OVERRUN"

Or:

> "Unhandled exception at 0x... — FastFail detected"

## What This Error Means

Fast-fail (introduced in Windows 8) is a security mitigation that terminates a process immediately when a severe security violation is detected, without running exception handlers. This prevents attackers from exploiting the vulnerability. The most common fast-fail code is `0xC0000409` (STATUS_STACK_BUFFER_OVERRUN), triggered when the `/GS` stack cookie is corrupted.

## Common Causes

- Stack buffer overrun detected by `/GS` stack cookie
- Control Flow Guard (CFG) violation — indirect call to invalid target
- Arbitrary Kernel Guard (AKG) violation
- Safe return detection failure
- `.idata` section write protection violation
- Malware exploitation attempt blocked by mitigations

## How to Fix

### Identify the Fast-Fail Code

```powershell
# Enable crash dumps
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" -Name "DumpFolder" -Value "C:\CrashDumps"
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" -Name "DumpType" -Value 2
```

Common fast-fail codes:

| Code | Name | Cause |
|------|------|-------|
| `0xC0000409` | STATUS_STACK_BUFFER_OVERRUN | Stack cookie corruption (`/GS`) |
| `0xC0000420` | STATUS_ASSERTION_FAILURE | Assertion failure |
| `0xC0000602` | STATUS_STACK_BUFFER_OVERRUN_HARD | Hardware-enforced stack protection |
| `0xC000041D` | STATUS_FAILED_FUNCTION_ENTRY | CFG violation |

### Enable Detailed Logging

```cmd
:: Enable crash dump analysis
:: Open the dump in WinDbg
:: Run: !analyze -v
:: Then: !chkimg
```

### Disable Control Flow Guard (Temporary Testing)

If a legitimate application triggers CFG:

```powershell
# Disable CFG for a specific application
Set-ProcessMitigation -Name "app.exe" -Disable CFG
```

### Update Drivers and Applications

Fast-fail often indicates a security vulnerability. Update all software to the latest version.

### Check Application Verifier Results

```cmd
appverif.exe /enable myapp.exe /rules Faults
```

## Related Errors

- [Buffer Overrun]({{< relref "/os/windows/runtime-error-buffer-overrun" >}}) — Stack buffer overflow triggering fast-fail
- [Unhandled Exception]({{< relref "/os/windows/runtime-error-unhandled-exception" >}}) — Unhandled exceptions at crash address
- [Access Violation]({{< relref "/os/windows/runtime-error-access-violation" >}}) — Memory access violations
