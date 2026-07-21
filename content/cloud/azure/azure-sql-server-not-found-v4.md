---
title: "[Solution] AZURE SQL Server Not Found"
description: "SQLServerNotFound for Azure SQL."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SQL Server Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Server name incorrect
- Deleted by admin
- Subscription mismatch

## How to Fix

### List servers

```bash
az sql server list -g myRG
```

## Examples

- Example scenario: server name incorrect
- Example scenario: deleted by admin
- Example scenario: subscription mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
