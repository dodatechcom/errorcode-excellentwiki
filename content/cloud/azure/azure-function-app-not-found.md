---
title: "[Solution] AZURE Function App Not Found"
description: "FunctionAppNotFound for Azure Functions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Function App Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Function name incorrect
- Deleted by admin
- Wrong resource group

## How to Fix

### List function apps

```bash
az functionapp list -g myRG
```

## Examples

- Example scenario: function name incorrect
- Example scenario: deleted by admin
- Example scenario: wrong resource group

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
