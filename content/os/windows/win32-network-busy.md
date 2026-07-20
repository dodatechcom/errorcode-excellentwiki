---
title: "[Solution] Error 54 — NETWORK_BUSY Fix"
description: "Fix Windows Error Code (NETWORK_BUSY) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 54
---

# [Solution] Error 54 — NETWORK_BUSY Fix

Win32 error 54 (`ERROR_NETWORK_BUSY`) occurs when the network is busy. This error is returned when the system cannot complete a network operation because the network is congested or the server is handling too many concurrent requests.

## Description

The NETWORK_BUSY error is returned when a network resource is temporarily unavailable due to high demand or congestion. This is common with file servers, database servers, and network shares under heavy load. The error code is `ERROR_NETWORK_BUSY` (value 54). The full message reads:

> "The network is busy."

## Common Causes

1. Too many simultaneous connections to the network resource.
2. Network bandwidth is saturated by other traffic.
3. The server has reached its maximum connection limit.
4. A network switch or router is congested.
5. Large file transfers are consuming available bandwidth.
6. A network loop or broadcast storm is overloading the network.

## Solutions

### Solution 1: Wait and Retry

Implement a retry mechanism with exponential backoff:

```powershell
$maxRetries = 5
for ($i = 0; $i -lt $maxRetries; $i++) {
    try {
        # Attempt network operation
        Get-ChildItem "\\Server\Share" -ErrorAction Stop
        Write-Host "Operation succeeded."
        break
    } catch {
        $waitTime = [math]::Pow(2, $i) * 2
        Write-Host "Network busy. Retrying in $waitTime seconds..."
        Start-Sleep -Seconds $waitTime
    }
}
```

### Solution 2: Check Network Load

Monitor network utilization to identify congestion:

```powershell
# Check network adapter utilization
Get-NetAdapter | Select-Object Name, LinkSpeed, Status

# Monitor active network connections
Get-NetTCPConnection | Group-Object RemoteAddress | Sort-Object Count -Descending | Select-Object -First 10
```

### Solution 3: Optimize Network Queries

Reduce the frequency and size of network requests:

```cmd
:: Use robocopy with bandwidth throttling
robocopy "\\Server\Share" "C:\Dest" /IPG:500 /MT:4
```

```powershell
# Limit concurrent operations
$jobs = @()
Get-ChildItem "\\Server\Share\*large*" | ForEach-Object {
    $jobs += Start-Job -ScriptBlock {
        param($path)
        Copy-Item $path "C:\Dest" -Force
    } -ArgumentList $_.FullName
}
$jobs | Wait-Job
```

### Solution 4: Reduce Server Connection Load

Close idle connections and reduce connection frequency:

```cmd
:: View active connections to a server
net use
net session \\Server
```

### Solution 5: Check for Network Loops

Verify network topology and check for broadcast storms:

```powershell
# Check for excessive broadcast traffic
Get-NetAdapter | ForEach-Object {
    Get-NetAdapterStatistics -Name $_.Name
}
```

## Related Errors

- [Error 65 — NETWORK_ACCESS_DENIED]({{< relref "/os/windows/win32-network-access-denied" >}}) — Network access is denied
- [Error 67 — BAD_NET_NAME]({{< relref "/os/windows/win32-bad-net-name" >}}) — Network name cannot be found
- [Error 121 — SEM_TIMEOUT]({{< relref "/os/windows/win32-sem-timeout" >}}) — The semaphore timeout period has expired
