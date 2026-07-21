---
title: "[Solution] HRESULT RPC_E_CONNECTION_CLOSED Fix"
description: "Fix HRESULT RPC_E_CONNECTION_CLOSED COM RPC error on Windows when the RPC connection is unexpectedly terminated between client and server."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] HRESULT RPC_E_CONNECTION_CLOSED Fix

The RPC_E_CONNECTION_CLOSED HRESULT error (0x80010108) occurs when the RPC connection between a COM client and server is closed unexpectedly. The client can no longer communicate with the remote object and any pending calls fail.

## Common Causes
- Network interruption between distributed COM components
- Firewall blocking RPC dynamic port range
- Server process crashing or restarting
- Idle connection timeout exceeding configured limits
- VPN connection dropping during active COM communication

## How to Fix

### Solution 1: Configure Firewall for DCOM

Allow DCOM traffic through Windows Firewall:

```powershell
New-NetFirewallRule -DisplayName "DCOM Inbound" -Direction Inbound -Protocol TCP -LocalPort 1024-65535 -Action Allow
```

### Solution 2: Increase DCOM Timeout

1. Open dcomcnfg
2. Right-click My Computer > Properties
3. On the COM tab, increase the Connection timeout values

### Solution 3: Configure Static DCOM Ports

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Rpc\Internet" /v "Internet" /t REG_SZ /d "5000-5100" /f
```

Set the RPC port range and configure firewall rules for those specific ports.

### Solution 4: Keep Connections Alive

Enable TCP keep-alive on the connection by adjusting registry settings for the specific application.

### Solution 5: Restart the DCOM Service

```powershell
Restart-Service -Name DcomLaunch -Force
```

## Examples
```powershell
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Rpc\Internet" | Format-List
```
