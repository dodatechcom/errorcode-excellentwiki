---
title: "COM Server Not Found Error - How to Fix"
description: "Fix 'COM server not found' errors on Windows 10 and 11. Locate missing COM servers, fix DCOM configuration, and resolve remote COM activation failures."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["com", "server-not-found", "dcom", "com-server"]
weight: 5
---

# COM Server Not Found Error

This error occurs when a client application cannot locate the COM server (local or remote) needed to instantiate a COM object. The error may read:

> "RPC server is unavailable (Exception from HRESULT: 0x800706BA)"

or

> "COM server not found."

This commonly affects DCOM configurations, distributed applications, and cross-machine COM communication.

## Common Causes

- **COM server not installed** — The application providing the COM server is not installed.
- **DCOM not enabled** — Distributed COM is disabled in system settings.
- **Network/firewall blocking** — DCOM ports are blocked by firewall.
- **Wrong machine name** — Client is configured to connect to wrong server.
- **COM server service not running** — The service hosting the COM object is stopped.

## How to Fix

### Enable DCOM

```powershell
Enable-PSRemoting -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Ole" -Name "EnableDCOM" -Value "Y"
```

### Check COM Server Registration

```cmd
reg query "HKCR\CLSID\{YOUR-CLSID-HERE}" /s
```

### Verify DCOM Configuration

Open DCOM configuration:

```cmd
dcomcnfg
```

Navigate to **Component Services > Computers > My Computer > DCOM Config** and verify the component exists.

### Check Firewall Rules for DCOM

```powershell
Enable-NetFirewallRule -DisplayName "DCOM In"
Enable-NetFirewallRule -DisplayName "DCOM Out"
```

Or manually open TCP ports 135 and dynamic RPC range (49152-65535).

### Test COM Server Connectivity

```powershell
Test-NetConnection -ComputerName "ServerName" -Port 135
```

### Restart DCOM Service

```powershell
Restart-Service DCOM -Force
```

### Check Event Viewer for COM Errors

```powershell
Get-WinEvent -LogName "System" -MaxEvents 50 | Where-Object { $_.ProviderName -like "*DCOM*" } | Format-List TimeCreated, Message
```

## Related Errors

- [COM Not Initialized]({{< relref "/os/windows/com-not-initialized" >}}) — COM library not initialized
- [COM Access Denied]({{< relref "/os/windows/com-access-denied" >}}) — Permission denied for COM access
- [COM Activation Error]({{< relref "/os/windows/com-activation-error" >}}) — COM object activation failure
