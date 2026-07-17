---
title: "[Solution] HRESULT RPC_S_SERVER_UNAVAILABLE (0x800706BA) — RPC Server Unavailable"
description: "Fix Windows HRESULT RPC_S_SERVER_UNAVAILABLE (0x800706BA) RPC server unavailable error. Causes and solutions for remote procedure call failures."
platforms: ["windows"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HRESULT RPC_S_SERVER_UNAVAILABLE (0x800706BA) — RPC Server Unavailable

**Error Code:** `0x800706BA`

RPC_S_SERVER_UNAVAILABLE indicates that the RPC server is not available to handle the remote procedure call. This error occurs when a client cannot reach the target server over the network.

## What This Error Means

This HRESULT maps to Win32 error `ERROR_RPC_S_SERVER_UNAVAILABLE`. The RPC endpoint mapper on the target machine is unreachable, the server service is stopped, or network connectivity has been lost. Common in Active Directory, WMI, and remote management scenarios.

## Common Causes

- The remote server is offline or powered down
- Windows Firewall blocking RPC ports (135 and dynamic range)
- The Server (LanmanServer) service is stopped on the target
- Network connectivity issues or DNS resolution failures

## How to Fix

### Verify Network Connectivity

```cmd
ping <remote-server>
telnet <remote-server> 135
```

### Ensure Required Services Are Running

```cmd
sc query RpcSs
sc query LanmanServer
net start RpcSs
net start LanmanServer
```

### Configure Windows Firewall for RPC

```cmd
netsh advfirewall firewall set rule name="RPC (TCP-In)" enable=yes
netsh advfirewall firewall add rule name="RPC Dynamic" dir=in action=allow protocol=tcp localport=49152-65535
```

### Reset RPC Configuration

```cmd
net stop RpcSs
net start RpcSs
```

## Related Errors

- [RPC_S_CALL_FAILED (0x800706BE)]({{< relref "/os/windows/hresult-rpc-s-call" >}}) — RPC call failed after reaching the server
- [E_ACCESSDENIED (0x80070005)]({{< relref "/os/windows/hresult-e-access-denied" >}}) — Access denied, permissions may block RPC connections
- [E_FAIL (0x80004005)]({{< relref "/os/windows/hresult-e-fail" >}}) — General failure during COM/RPC operations
