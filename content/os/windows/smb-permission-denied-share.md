---
title: "[Solution] SMB Share Permission Denied Error Fix"
description: "Fix SMB network share access denied error on Windows. Resolve permission issues when connecting to shared folders over the network on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] SMB Share Permission Denied Error Fix

The SMB share permission denied error means you have network connectivity to the file server but lack the necessary permissions to access the share. This is a common issue in domain and workgroup environments.

## Common Causes
- Share permissions do not include your user account
- NTFS permissions on the shared folder are restrictive
- Authenticated Users group removed from share permissions
- Group Policy applying Deny permissions
- Credential mismatch between stored and required credentials

## How to Fix

### Solution 1: Check Share Permissions

```powershell
Get-SmbShareAccess -Name "ShareName"
```

### Solution 2: Add Permissions to the Share

```powershell
Grant-SmbShareAccess -Name "ShareName" -AccountName "DOMAIN\username" -AccessRight Full -Force
```

### Solution 3: Clear Saved Credentials

```cmd
cmdkey /list
cmdkey /delete:ServerName
```

### Solution 4: Test with Net Use

```cmd
net use \\server\share /user:domain\username password
```

### Solution 5: Check Effective Permissions

Right-click the shared folder > Properties > Security > Advanced > Effective Access and enter your username.

## Examples
```powershell
Get-SmbShare | Get-SmbShareAccess | Select-Object Name, AccountName, AccessRight, AccessControlType
```
