---
title: "[Solution] SMB Connection Timeout Error Fix"
description: "Fix SMB connection timeout error on Windows when file share connections fail to establish within the allowed time period on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] SMB Connection Timeout Error Fix

An SMB connection timeout means the client could not establish a connection to the SMB server within the configured timeout period. The connection attempt hangs or takes too long to complete.

## Common Causes
- Network latency too high for the SMB timeout setting
- Firewall blocking SMB ports 445 or 139
- DNS resolution delays for the server hostname
- SMB server overloaded with existing connections
- Network congestion or packet loss on the path

## How to Fix

### Solution 1: Increase SMB Timeout

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" /v SessTimeout /t REG_DWORD /d 300 /f
```

### Solution 2: Test Network Connectivity

```cmd
ping -n 10 <server-ip>
```

### Solution 3: Flush DNS Cache

```cmd
ipconfig /flushdns
ipconfig /registerdns
```

### Solution 4: Configure SMB KeepAlive

```powershell
Set-SmbServerConfiguration -EnableSMB2Protocol $true -Force
```

### Solution 5: Use IP Address Instead of Hostname

```cmd
net use \\192.168.1.100\share /user:domain\user password
```

## Examples
```powershell
Test-NetConnection -ComputerName fileserver -Port 445
```
