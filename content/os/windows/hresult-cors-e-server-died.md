---
title: "[Solution] HRESULT CORS_E_SERVER_DIED COM+ Fix"
description: "Fix HRESULT CORS_E_SERVER_DIED COM+ server death error on Windows. Resolve COM+ application pool crashes and server termination issues."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] HRESULT CORS_E_SERVER_DIED COM+ Fix

The CORS_E_SERVER_DIED HRESULT error occurs when a COM+ application server process dies unexpectedly. This prevents COM+ components from processing requests and affects any application relying on the COM+ services hosted by that server.

## Common Causes
- COM+ application pool recycling due to memory limits
- Unhandled exception in a COM+ component method
- Corrupted COM+ application registration
- Identity account password mismatch for COM+ configured applications
- System resource exhaustion causing process termination

## How to Fix

### Solution 1: Restart COM+ Application

Open Component Services, navigate to Component Services > Computers > My Computer > COM+ Applications. Right-click the affected application and select Restart.

### Solution 2: Check COM+ Application Identity

In Component Services, open the COM+ application properties and verify the Identity tab has correct credentials.

### Solution 3: Rebuild COM+ Application

1. Export the COM+ application from Component Services
2. Remove it from the COM+ catalog
3. Re-import the exported application

### Solution 4: Clear COM+ Catalog Corruption

```cmd
net stop COMSysApp
cd %systemroot%\system32
regsvr32 comsvcs.dll
net start COMSysApp
```

### Solution 5: Increase Application Pool Limits

In Component Services, open the COM+ application properties and increase the memory limit under the Activation tab to prevent premature recycling.

## Examples
```powershell
Get-Service -Name COMSysApp | Restart-Service -Force
```
