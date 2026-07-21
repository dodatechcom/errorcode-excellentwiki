---
title: "[Solution] AZURE Connection Failed"
description: "ConnectionFailed for SQL database."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Connection Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Server not reachable
- Port 1433 blocked
- VNet/service endpoint missing

## How to Fix

### Test connection

```bash
sqlcmd -S myServer.database.windows.net -U admin -P pass
```

## Examples

- Example scenario: server not reachable
- Example scenario: port 1433 blocked
- Example scenario: vnet/service endpoint missing

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
