---
title: "[Solution] HRESULT RPC_E_SERVER_UNAVAILABLE Fix"
description: "Fix HRESULT RPC_E_SERVER_UNAVAILABLE COM error on Windows when the COM server cannot be reached or is not responding to requests."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] HRESULT RPC_E_SERVER_UNAVAILABLE Fix

The RPC_E_SERVER_UNAVAILABLE HRESULT error (0x800706BA) means the COM server is unreachable. The RPC endpoint mapper on the target machine cannot locate the requested service or the server is not running.

## Common Causes
- The COM server application is not running or has crashed
- Windows Firewall blocking RPC traffic on required ports
- RPC service is stopped on the remote machine
- Network connectivity issues between client and server
- DNS resolution failure for the server hostname

## How to Fix

### Solution 1: Verify RPC Service Is Running

```powershell
Get-Service -Name RpcSs, RpcEptMapper | Select-Object Name, Status, StartType
```

Start the services if they are stopped:

```powershell
Start-Service -Name RpcSs
Start-Service -Name RpcEptMapper
```

### Solution 2: Test Network Connectivity

```cmd
ping <server-name>
telnet <server-name> 135
```

Ensure port 135 (RPC Endpoint Mapper) is reachable on the remote server.

### Solution 3: Configure Windows Firewall

```powershell
Enable-NetFirewallRule -DisplayGroup "Remote Volume Management"
Enable-NetFirewallRule -DisplayGroup "DCOM"
```

### Solution 4: Check DNS Resolution

```cmd
nslookup <server-name>
ipconfig /flushdns
```

### Solution 5: Restart DCOM Service

```powershell
Stop-Service -Name DcomLaunch -Force
Start-Service -Name DcomLaunch
```

## Examples
```powershell
Get-Service RpcSs | Restart-Service -Force
```
