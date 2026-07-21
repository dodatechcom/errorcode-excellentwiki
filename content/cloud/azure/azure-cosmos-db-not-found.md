---
title: "[Solution] AZURE Cosmos DB Not Found"
description: "CosmosDBAccountNotFound for Cosmos DB."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cosmos DB Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Account name incorrect
- Deleted by admin
- Region mismatch

## How to Fix

### List accounts

```bash
az cosmosdb list
```

## Examples

- Example scenario: account name incorrect
- Example scenario: deleted by admin
- Example scenario: region mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
