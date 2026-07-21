---
title: "[Solution] COM Server Timeout Error 0x8001010a Fix"
description: "Fix HRESULT RPC_E_CALL_REJECTED or COM server timeout error 0x8001010a when COM calls are rejected due to server overload on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] COM Server Timeout Error 0x8001010a Fix

The HRESULT RPC_E_CALL_REJECTED (0x8001010a) error occurs when a COM server is too busy to process incoming requests. The server rejects the RPC call because its call queue is full or the server thread pool is exhausted.

## Common Causes
- COM server overwhelmed by too many concurrent requests
- Server application stuck in a long-running operation
- Thread pool exhaustion preventing new call acceptance
- DCOM configuration with insufficient concurrent call limit
- Memory pressure causing the server to throttle incoming calls

## How to Fix

### Solution 1: Increase DCOM Thread Pool

Open Component Services, right-click My Computer > Properties. On the COM tab, increase the maximum number of connections.

### Solution 2: Restart the COM Server

```powershell
Stop-Process -Name "serverprocess" -Force
Start-Process -FilePath "C:\Path\To\server.exe"
```

### Solution 3: Check Server Resource Usage

```powershell
Get-Process | Where-Object { $_.Name -eq 'serverprocess' } | Select-Object Name, CPU, @{N='WS(MB)';E={[math]::Round($_.WorkingSet64/1MB)}}, HandleCount, Threads
```

### Solution 4: Increase Client Timeout

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Ole" /v ServerCallTimeout /t REG_DWORD /d 300000 /f
```

Set the timeout to 300 seconds (300000 milliseconds).

### Solution 5: Balance Load Across Multiple Server Instances

Deploy the COM server on multiple machines and configure DCOM load balancing or use a COM+ application partitioning scheme.

## Examples
```powershell
Get-Process | Where-Object { $_.Name -eq 'serverprocess' } | Select-Object Name, CPU, HandleCount, Threads
dcomcnfg
```
