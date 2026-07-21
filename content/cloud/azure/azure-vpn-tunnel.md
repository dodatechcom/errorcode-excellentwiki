---
title: "[Solution] AZURE VPN Tunnel"
description: "VPNTunnelError for VPN tunnels."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VPN Tunnel` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Tunnel disconnected
- Shared key mismatch
- BGP session down

## How to Fix

### Check connection

```bash
az network vpn-connection show -n myConn -g myRG
```

## Examples

- Example scenario: tunnel disconnected
- Example scenario: shared key mismatch
- Example scenario: bgp session down

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
