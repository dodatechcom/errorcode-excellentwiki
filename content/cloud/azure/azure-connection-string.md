---
title: "[Solution] AZURE Connection String"
description: "ConnectionStringError for connection strings."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Connection String` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Account key mismatch
- Endpoint suffix wrong
- Table/blob endpoint missing

## How to Fix

### Show connection

```bash
az storage account show-connection-string -g myRG -n myAccount
```

## Examples

- Example scenario: account key mismatch
- Example scenario: endpoint suffix wrong
- Example scenario: table/blob endpoint missing

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
