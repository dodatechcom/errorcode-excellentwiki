---
title: "[Solution] HRESULT RPC_E_SERVER_DIED Error Fix"
description: "Fix HRESULT RPC_E_SERVER_DIED error when a remote COM server process terminates unexpectedly during an RPC call on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] HRESULT RPC_E_SERVER_DIED Error Fix

The RPC_E_SERVER_DIED HRESULT error (0x80010001) occurs when a COM server process terminates unexpectedly while an RPC call is in progress. The client application receives this error because the server it was communicating with has crashed or been forcefully terminated.

## Common Causes
- The COM server application crashed due to an unhandled exception
- Insufficient system memory causing the server process to be terminated
- Access permissions preventing the server from running under the caller security context
- DCOM configuration blocking remote activation
- Antivirus software terminating the server process

## How to Fix

### Solution 1: Check Event Viewer for Server Crash Details

Open Event Viewer and check the Application log for crash reports from the COM server application. The faulting module and exception code will help identify the root cause.

### Solution 2: Verify DCOM Permissions

```powershell
dcomcnfg
```

Navigate to Component Services > Computers > My Computer > DCOM Config. Find the application, right-click Properties, and verify the Security and Identity tabs have correct settings.

### Solution 3: Increase Memory for the Server

If the server runs on a resource-constrained system, increase available RAM or adjust the memory limits in the application configuration.

### Solution 4: Re-register the COM Server

```cmd
regsvr32 /i:scn serverdll.dll
```

Replace serverdll.dll with the actual server DLL path. Restart the application after re-registration.

### Solution 5: Check for Application Updates

Install the latest version of the application hosting the COM server, as crashes are often fixed in newer releases.

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='Application'; Level=2; StartTime=(Get-Date).AddDays(-7)} | Where-Object { $_.Message -like '*Faulting application*' } | Format-Table TimeCreated, Message -Wrap
```
