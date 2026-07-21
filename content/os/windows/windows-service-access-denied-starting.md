---
title: "[Solution] Windows Service Access Denied Starting Fix"
description: "Fix Windows service that returns access denied when trying to start. Resolve service logon permissions and service account issues on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Service Access Denied Starting Fix

A service access denied error on startup means the service account does not have the required permissions to run the service.

## Common Causes
- Service account missing Log on as a service right
- Service binary path permissions incorrect
- Account password recently changed but service not updated
- Group Policy denying service logon rights
- Service configured with an invalid account

## How to Fix

### Solution 1: Grant Log on as a Service Right

```cmd
secedit /export /cfg C:\secpol.cfg
```

Edit the file to add the service account to SeServiceLogonRight, then import:

```cmd
secedit /configure /db secedit.sdb /cfg C:\secpol.cfg /areas USER_RIGHTS
```

### Solution 2: Update Service Credentials

```cmd
sc.exe config "ServiceName" obj= "DOMAIN\svcaccount" password= "NewPassword"
```

### Solution 3: Use LocalSystem Temporarily

```cmd
sc.exe config "ServiceName" obj= LocalSystem
```

### Solution 4: Check Service Binary Permissions

Ensure the service account has Read and Execute permissions on the service binary.

### Solution 5: Review Group Policy

```powershell
gpresult /h C:\gpreport.html
```

## Examples
```powershell
Get-WmiObject Win32_Service | Where-Object { $_.State -eq 'Stopped' -and $_.StartMode -eq 'Auto' } | Select-Object Name, StartName, PathName
```
