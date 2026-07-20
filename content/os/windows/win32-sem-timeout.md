---
title: "[Solution] Error 121 — SEM_TIMEOUT Fix"
description: "Fix Windows Error Code (SEM_TIMEOUT) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 121
---

# [Solution] Error 121 — SEM_TIMEOUT Fix

Win32 error 121 (`ERROR_SEM_TIMEOUT`) occurs when the semaphore timeout period has expired. Semaphores are synchronization primitives used to control access to shared resources, and this error means a wait operation exceeded its time limit.

## Description

The SEM_TIMEOUT error is returned when a thread waiting on a semaphore does not receive a signal within the specified timeout period. This is common in multi-threaded applications, network operations, and database connections where resource contention causes delays. The error code is `ERROR_SEM_TIMEOUT` (value 121). The full message reads:

> "The semaphore timeout period has expired."

## Common Causes

1. A remote server or service did not respond within the expected time.
2. Network latency or packet loss caused a delayed response.
3. A database connection was not released and timed out.
4. Resource contention caused threads to wait too long for a semaphore.
5. A deadlocked process holds the semaphore indefinitely.
6. The system is under heavy load and cannot respond in time.

## Solutions

### Solution 1: Increase Timeout Values

Increase the timeout for the operation in your application or configuration:

```powershell
# Increase command timeout in PowerShell remoting
$session = New-PSSession -ComputerName "Server" -OperationTimeout 60000
```

```cmd
:: Increase network timeout in registry
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v TcpTimedWaitDelay /t REG_DWORD /d 120 /f
```

### Solution 2: Check Network Latency

Test network connectivity and latency to the target host:

```cmd
ping -n 10 TargetServer
tracert TargetServer
```

```powershell
# Measure network latency
Test-Connection -ComputerName "TargetServer" -Count 10 | Select-Object ResponseTime
```

### Solution 3: Optimize the Operation

Reduce the scope of the operation to complete faster:

```powershell
# Split large operations into smaller batches
$items = Get-ChildItem "C:\LargeFolder" -Recurse
 batchSize = 100
for ($i = 0; $i -lt $items.Count; $i += $batchSize) {
    $batch = $items[$i..($i + $batchSize - 1)]
    # Process batch
}
```

### Solution 4: Check for Deadlocked Processes

```powershell
# Check for hung processes
Get-Process | Where-Object { $_.Responding -eq $false } | Select-Object Name, Id, CPU
```

### Solution 5: Restart the Service

Restart the service that caused the timeout:

```cmd
net stop "ServiceName" && net start "ServiceName"
```

## Related Errors

- [Error 109 — BROKEN_PIPE]({{< relref "/os/windows/win32-broken-pipe" >}}) — The pipe has been ended
- [Error 122 — INSUFFICIENT_BUFFER]({{< relref "/os/windows/win32-insufficient-buffer-error" >}}) — Data area too small
- [Error 995 — OPERATION_ABORTED]({{< relref "/os/windows/win32-operation-aborted" >}}) — I/O operation was aborted
