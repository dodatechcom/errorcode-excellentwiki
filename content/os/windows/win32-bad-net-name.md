---
title: "[Solution] Error 67 — BAD_NET_NAME Fix"
description: "Fix Windows Error Code (BAD_NET_NAME) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 67
---

# [Solution] Error 67 — BAD_NET_NAME Fix

Win32 error 67 (`ERROR_BAD_NET_NAME`) occurs when the network name cannot be found. This means Windows cannot resolve the share name, server name, or network path provided in the connection request.

## Description

The BAD_NET_NAME error is returned when the system cannot locate a network resource by the name specified. This can be due to an incorrect share name, DNS resolution failure, or the server being offline. The error code is `ERROR_BAD_NET_NAME` (value 67). The full message reads:

> "The network name cannot be found."

## Common Causes

1. The share name is spelled incorrectly.
2. The target server is offline or unreachable.
3. DNS cannot resolve the server name.
4. The network share no longer exists.
5. The server service is not running on the target.
6. A network drive mapping points to a deleted or renamed share.

## Solutions

### Solution 1: Verify the Share Name

Confirm the share name is correct and the share exists:

```cmd
:: List shares on a remote server
net view \\ServerName
```

```powershell
# Check if a specific share is accessible
Test-Path "\\ServerName\ShareName"
```

### Solution 2: Check DNS Resolution

Verify the server name resolves correctly:

```cmd
nslookup ServerName
ping ServerName
ipconfig /flushdns
```

```powershell
# Resolve server name to IP
Resolve-DnsName -Name "ServerName"
```

### Solution 3: Ping the Server

Test basic network connectivity:

```cmd
ping -n 4 ServerName
```

```powershell
# Test connectivity
Test-Connection -ComputerName "ServerName" -Count 4 -Quiet
```

### Solution 4: Verify the Server Service

Ensure the server service is running on the target:

```cmd
:: Check server service on remote machine
sc \\ServerName query lanmanserver
```

```powershell
# Restart server service if needed
Invoke-Command -ComputerName "ServerName" -ScriptBlock {
    Restart-Service -Name "LanmanServer" -Force
}
```

### Solution 5: Re-map the Network Drive

Remove the old mapping and create a fresh one:

```cmd
:: Remove all network mappings
net use * /delete /yes

:: Map the drive with explicit path
net use Z: \\ServerName\ShareName /persistent:yes
```

## Related Errors

- [Error 5 — ACCESS_DENIED]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Access is denied
- [Error 65 — NETWORK_ACCESS_DENIED]({{< relref "/os/windows/win32-network-access-denied" >}}) — Network access is denied
- [Error 54 — NETWORK_BUSY]({{< relref "/os/windows/win32-network-busy" >}}) — The network is busy
