---
title: "[Solution] RDP Disconnect Logon Timeout Error Fix"
description: "Fix Remote Desktop disconnect error caused by logon timeout on Windows. Resolve RDP session timeouts and idle session disconnection issues."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] RDP Disconnect Logon Timeout Error Fix

RDP disconnect due to logon timeout occurs when the Remote Desktop session is terminated because the logon process takes too long to complete. Users see a disconnected session before they can interact with the desktop.

## Common Causes
- Slow Group Policy processing during logon
- Roaming profile taking too long to download
- User profile corruption causing extended logon
- Network latency between client and RDS server
- Logon script timeout causing session disconnect

## How to Fix

### Solution 1: Increase Logon Timeout via Registry

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v LogonTimeout /t REG_DWORD /d 120 /f
```

### Solution 2: Optimize Group Policy Processing

```cmd
gpresult /h C:\gpreport.html
```

Disable slow-link detection for Group Policy over RDP connections.

### Solution 3: Use Local Profiles for Testing

Configure RDS to use local profiles instead of roaming profiles to test if the profile is causing the timeout.

### Solution 4: Increase Keep-Alive Settings

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v KeepAliveTimeout /t REG_DWORD /d 1 /f
```

### Solution 5: Check Network Latency

```cmd
ping rds-server -n 20
```

High latency between the client and RDS server can cause logon timeout disconnects.

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TerminalServices-LocalSessionManager/Operational'; Id=21,23} -MaxEvents 10 | Format-Table TimeCreated, Message -Wrap
```
