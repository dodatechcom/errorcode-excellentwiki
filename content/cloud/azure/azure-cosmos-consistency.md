---
title: "[Solution] AZURE Cosmos Consistency"
description: "CosmosConsistencyError for consistency config."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cosmos Consistency` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Consistency level not supported
- Strong unavailable globally

## How to Fix

### Show consistency

```bash
az cosmosdb show -n myAccount --query consistencyPolicy
```

## Examples

- Example scenario: consistency level not supported
- Example scenario: strong unavailable globally

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
