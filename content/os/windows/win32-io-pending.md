---
title: "[Solution] Error 997 — IO_PENDING Fix"
description: "Fix Windows Error Code (IO_PENDING) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 997
---

# [Solution] Error 997 — IO_PENDING Fix

Win32 error 997 (`ERROR_IO_PENDING`) occurs when an overlapped I/O operation is in progress. Unlike most errors, this is often an informational status indicating the operation has been successfully queued but not yet completed.

## Description

The IO_PENDING error is returned when an asynchronous (overlapped) I/O operation has been accepted and is being processed in the background. The calling code must wait for or poll the operation to complete before reading the result. If the calling code treats this as an error, the operation will appear to fail even though it is still running. The error code is `ERROR_IO_PENDING` (value 997). The full message reads:

> "Overlapped I/O operation is in progress."

## Common Causes

1. The application uses asynchronous I/O but does not handle the pending status.
2. The `GetOverlappedResult` function was not called to wait for completion.
3. The event object used for synchronization was not properly initialized.
4. The I/O completion callback was not registered correctly.
5. A blocking call was made on an overlapped handle.
6. The system is under heavy load and operations take longer than expected.

## Solutions

### Solution 1: Wait for Completion

Use `GetOverlappedResult` to wait for the asynchronous operation to finish:

```powershell
# PowerShell: Wait for async file operation
$handle = [System.IO.File]::Open("C:\file.txt", [System.IO.FileMode]::Open, [System.IO.FileAccess]::Read, [System.IO.FileShare]::None, 4096, [System.IO.FileOptions]::Asynchronous)
$buffer = New-Object byte[] 4096
$ar = $handle.BeginRead($buffer, 0, 4096, $null, $null)
# Wait for the operation to complete
$bytesRead = $handle.EndRead($ar)
$handle.Close()
```

### Solution 2: Use GetOverlappedResult

Check the status of an overlapped operation:

```powershell
# Check if overlapped operation completed
$overlapped = New-Object System.Threading.ManualResetEvent($false)
# ... initiate overlapped I/O ...
$overlapped.WaitOne() | Out-Null
# Operation completed
```

### Solution 3: Handle Async Operations Properly

Use proper async patterns with callbacks:

```powershell
# Use async file read with callback
$task = [System.IO.File]::ReadAllBytesAsync("C:\Path\To\file.txt")
# The task runs in the background
$task.Wait()
$result = $task.Result
```

### Solution 4: Use Thread.Sleep to Poll

Poll for completion if GetOverlappedResult is not available:

```powershell
while ($true) {
    if ($handle.SafeWaitHandle.IsInvalid) { break }
    Start-Sleep -Milliseconds 100
}
```

### Solution 5: Increase Timeout

If operations are timing out, increase the wait timeout:

```powershell
# Increase timeout in WaitHandle
$completed = [System.Threading.WaitHandle]::WaitAny(@{$overlapped.Handle}, 30000)
if ($completed -eq [System.Threading.WaitHandle]::WaitTimeout) {
    Write-Host "Operation timed out."
}
```

## Related Errors

- [Error 995 — OPERATION_ABORTED]({{< relref "/os/windows/win32-operation-aborted" >}}) — I/O operation was aborted
- [Error 998 — NOACCESS]({{< relref "/os/windows/win32-noaccess" >}}) — Invalid access to memory location
- [Error 121 — SEM_TIMEOUT]({{< relref "/os/windows/win32-sem-timeout" >}}) — The semaphore timeout period has expired
