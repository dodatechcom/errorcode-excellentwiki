---
title: "[Solution] Unhandled Exception at 0x... — Fix Application Crash"
description: "Fix unhandled exception crashes on Windows 10/11. Diagnose and resolve crash addresses, exception codes, and unhandled exception handlers."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["unhandled-exception", "crash", "exception-code", "0xC0000005", "debug"]
weight: 5
---

# Unhandled Exception at 0x... — Application Crash

An unhandled exception occurs when a program encounters an error condition that is not caught by any exception handler. Windows displays:

> "Unhandled exception at 0xADDRESS in program.exe: 0xEXCEPTION_CODE"

Or in a Windows Error Reporting dialog:

> "program.exe has stopped working. A problem caused the program to stop working correctly."

## What This Error Means

Every exception in Windows (memory access violations, divide by zero, illegal instruction, etc.) must be handled by the application's structured exception handling (SEH) chain. If no handler catches the exception, Windows terminates the process and may generate a crash dump. The crash address `0xADDRESS` tells you where in the code the exception occurred, and the exception code tells you what type of error it was.

## Common Causes

- Access violation (`0xC0000005`) — most common unhandled exception
- Integer divide by zero (`0xC000008E`)
- Illegal instruction (`0xC000001D`)
- Stack overflow (`0xC00000FD`)
- Unhandled C++ exception (no `try/catch` block)
- Third-party DLL crashing inside the application process

## How to Fix

### Decode the Exception Code

```powershell
# Common exception codes
# 0xC0000005 - STATUS_ACCESS_VIOLATION
# 0xC000008E - STATUS_FLOAT_DIVIDE_BY_ZERO
# 0xC000001D - STATUS_ILLEGAL_INSTRUCTION
# 0xC00000FD - STATUS_STACK_OVERFLOW
# 0xC0000409 - STATUS_STACK_BUFFER_OVERRUN
# 0xE0434352 - CLR exception (.NET)
# 0xE06D7363 - C++ EH exception
```

### Analyze the Crash Dump

```powershell
# Enable crash dumps
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" -Name "DumpFolder" -Value "C:\CrashDumps"
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" -Name "DumpType" -Value 2
```

Open the dump in WinDbg and run:

```
!analyze -v
```

### Add Exception Handling (for Developers)

```c
// C structured exception handling
__try {
    // risky code
} __except (EXCEPTION_EXECUTE_HANDLER) {
    // handle the exception
}

// C++ exception handling
try {
    // risky code
} catch (const std::exception& e) {
    // handle the exception
}
```

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Update or Reinstall the Application

Check for updates from the software vendor. Many unhandled exceptions are fixed in newer versions.

## Related Errors

- [Access Violation]({{< relref "/os/windows/runtime-error-access-violation" >}}) — Most common cause of unhandled exceptions
- [FastFail Error]({{< relref "/os/windows/runtime-error-fast-fail" >}}) — Security fast-fail terminations
- [Application Error Event 1000]({{< relref "/os/windows/event-1000" >}}) — Event log entries for application crashes
