---
title: "[Solution] Error 109 — BROKEN_PIPE Fix"
description: "Fix Windows Error Code (BROKEN_PIPE) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 109
---

# [Solution] Error 109 — BROKEN_PIPE Fix

Win32 error 109 (`ERROR_BROKEN_PIPE`) occurs when the pipe has been ended. Named pipes are a fundamental inter-process communication mechanism in Windows, and this error indicates the other end of the pipe has disconnected or closed.

## Description

The BROKEN_PIPE error is returned when a process attempts to read from or write to a named pipe, but the other end of the pipe has been closed or terminated. This is common in client-server applications, background services, and command-line tools that communicate via pipes. The error code is `ERROR_BROKEN_PIPE` (value 109). The full message reads:

> "The pipe has been ended."

## Common Causes

1. The server process that owns the pipe has crashed or been terminated.
2. The client disconnected before the server finished writing data.
3. A service that provides the pipe endpoint was stopped.
4. Network issues interrupted a pipe over a network share.
5. A timeout caused the pipe connection to be closed.
6. Insufficient system resources for pipe communication.

## Solutions

### Solution 1: Verify Pipe Connection

Check if the named pipe exists and is available:

```powershell
# List named pipes on the system
Get-ChildItem \\.\pipe\ | Select-Object Name
```

### Solution 2: Restart the Service

Restart the service that hosts the named pipe endpoint:

```powershell
# Restart a specific service
Restart-Service -Name "ServiceName" -Force
```

```cmd
# Or using sc
net stop "ServiceName"
net start "ServiceName"
```

### Solution 3: Verify Client Connection

Ensure the client is connecting to the correct pipe name and server:

```powershell
# Test pipe connectivity
$pipePath = "\\.\pipe\PipeName"
if (Test-Path $pipePath) {
    Write-Host "Pipe exists and is accessible."
} else {
    Write-Host "Pipe not found."
}
```

### Solution 4: Increase Pipe Timeout

Increase the pipe timeout to prevent premature disconnection:

```powershell
# Set pipe timeout in registry (in milliseconds)
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" -Name "PipeTimeout" -Value 120000 -Type DWord
```

### Solution 5: Check Service Dependencies

Verify the service dependencies are running:

```cmd
sc qc "ServiceName"
sc queryex "ServiceName"
```

## Related Errors

- [Error 121 — SEM_TIMEOUT]({{< relref "/os/windows/win32-sem-timeout" >}}) — The semaphore timeout period has expired
- [Error 122 — INSUFFICIENT_BUFFER]({{< relref "/os/windows/win32-insufficient-buffer-error" >}}) — Data area too small
- [Error 995 — OPERATION_ABORTED]({{< relref "/os/windows/win32-operation-aborted" >}}) — I/O operation was aborted
