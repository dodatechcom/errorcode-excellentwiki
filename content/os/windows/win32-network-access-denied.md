---
title: "[Solution] Error 65 — NETWORK_ACCESS_DENIED Fix"
description: "Fix Windows Error Code (NETWORK_ACCESS_DENIED) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 65
---

# [Solution] Error 65 — NETWORK_ACCESS_DENIED Fix

Win32 error 65 (`ERROR_NETWORK_ACCESS_DENIED`) occurs when network access is denied. This error is returned when a user or process attempts to access a network resource but is denied by permissions, share settings, or firewall rules.

## Description

The NETWORK_ACCESS_DENIED error is returned when a network connection to a shared resource is rejected. This can occur due to share-level permissions, NTFS permissions, firewall rules, or Group Policy restrictions. The error code is `ERROR_NETWORK_ACCESS_DENIED` (value 65). The full message reads:

> "Network access is denied."

## Common Causes

1. The share permissions do not allow the user access.
2. NTFS permissions on the shared folder deny access.
3. Windows Firewall is blocking the network connection.
4. User Account Control (UAC) is filtering the user's token.
5. Group Policy restricts network access for the user.
6. The server requires authentication that was not provided.

## Solutions

### Solution 1: Check Share Permissions

Verify and modify the share permissions:

```cmd
:: View share permissions
net share ShareName

:: Modify share permissions
net share ShareName /grant:Everyone,READ
```

### Solution 2: Verify Share Settings

Check the share configuration in PowerShell:

```powershell
# View all shares and their permissions
Get-SmbShare | Get-SmbShareAccess

# Add read permission
Grant-SmbShareAccess -Name "ShareName" -AccountName "DOMAIN\Username" -AccessRight Read -Force
```

### Solution 3: Check Firewall Rules

Ensure the firewall allows file and printer sharing:

```powershell
# Check firewall rules for file sharing
Get-NetFirewallRule | Where-Object { $_.DisplayName -like "*File*" -and $_.Enabled -eq "True" }

# Enable file and printer sharing
Enable-NetFirewallRule -DisplayGroup "File and Printer Sharing"
```

```cmd
:: Allow file sharing through firewall
netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=yes
```

### Solution 4: Use Explicit Credentials

Provide credentials explicitly when connecting:

```cmd
net use \\Server\Share /user:DOMAIN\Username password
```

```powershell
$cred = Get-Credential
New-PSDrive -Name "Z" -PSProvider FileSystem -Root "\\Server\Share" -Credential $cred
```

### Solution 5: Check UAC Token Filtering

UAC can strip admin credentials for network access. Enable the admin approval mode setting:

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
"LocalAccountTokenFilterPolicy"=dword:00000001
```

Apply:

```cmd
reg import enable_local_token.reg
```

## Related Errors

- [Error 5 — ACCESS_DENIED]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Access is denied
- [Error 67 — BAD_NET_NAME]({{< relref "/os/windows/win32-bad-net-name" >}}) — Network name cannot be found
- [Error 54 — NETWORK_BUSY]({{< relref "/os/windows/win32-network-busy" >}}) — The network is busy
