---
title: "ERROR_TIMEOUT (1460) - How to Fix"
description: "Fix Windows ERROR_TIMEOUT (1460). Resolve timeout errors, increase wait times, and fix operations that exceed time limits on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-1460", "timeout", "wait"]
weight: 5
---

# ERROR_TIMEOUT (Win32 Error 1460)

This Win32 API error occurs when an operation exceeds its allotted time limit. The error code is `ERROR_TIMEOUT` (value 1460). The full message reads:

> "This operation returned because the timeout period expired."

This commonly appears in network operations, service starts, COM calls, and system operations that take too long to complete.

## Common Causes

- **Slow network response** — Remote server took too long to respond.
- **Service startup timeout** — Service didn't start within the default timeout.
- **Resource contention** — Resource locked by another process for too long.
- **System overload** — System too busy to complete operation in time.
- **Firewall blocking** — Network requests blocked, causing timeout waiting for response.

## How to Fix

### Increase Timeout Value

```powershell
# Increase web request timeout
$response = Invoke-WebRequest -Uri "https://example.com" -TimeoutSec 300
```

### Increase Service Startup Timeout

```powershell
$service = Get-WmiObject Win32_Service -Filter "Name='ServiceName'"
$service.StartService()
Start-Sleep -Seconds 60
```

### Check Network Connectivity

```powershell
Test-NetConnection -ComputerName "ServerName" -Port 443
Test-Connection -ComputerName "ServerName" -Count 4
```

### Retry with Exponential Backoff

```powershell
function Invoke-WithRetry {
    param([scriptblock]$Action, [int]$MaxRetries = 5)
    for ($i = 0; $i -lt $MaxRetries; $i++) {
        try {
            return & $Action
        } catch {
            $wait = [math]::Pow(2, $i) * 1000
            Start-Sleep -Milliseconds $wait
        }
    }
    throw "Max retries exceeded"
}
```

### Increase Registry Timeout

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control" /v "ServicesPipeTimeout" /t REG_DWORD /d 120000 /f
```

### Check System Performance

```powershell
Get-Counter "\Processor(_Total)\% Processor Time" -SampleInterval 5 -MaxSamples 3
Get-Counter "\Memory\Available MBytes" -SampleInterval 5 -MaxSamples 3
```

### Disable Timeout for Debugging

```powershell
$job = Start-Job -ScriptBlock { Start-Sleep -Seconds 300 }
$job | Wait-Job -Timeout 600
```

## Related Errors

- [ERROR_BUSY (170)]({{< relref "/os/windows/win32-busy" >}}) — Resource busy causing delays
- [ERROR_NOT_ENOUGH_MEMORY (8)]({{< relref "/os/windows/win32-not-enough-memory" >}}) — Memory issues causing slow operations
- [Windows Update Timeout]({{< relref "/os/windows/win32-windows-update-timeout" >}}) — Update-specific timeout
