---
title: "[Solution] AZURE Table Not Found"
description: "TableNotFound for Log Analytics tables."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Table Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Table name incorrect
- Table not yet ingested
- Custom log table not created

## How to Fix

### List tables

```bash
az monitor log-analytics workspace table list -g myRG -w myWorkspace
```

## Examples

- Example scenario: table name incorrect
- Example scenario: table not yet ingested
- Example scenario: custom log table not created

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
