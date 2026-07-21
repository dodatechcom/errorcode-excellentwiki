---
title: "[Solution] AZURE Cosmos Indexing"
description: "CosmosIndexingError for indexing."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cosmos Indexing` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Indexing policy invalid
- Index path mismatch
- Composite index conflict

## How to Fix

### Update indexing

```bash
az cosmosdb sql container update -a myAccount -d myDB -n myContainer --idx @indexing.json
```

## Examples

- Example scenario: indexing policy invalid
- Example scenario: index path mismatch
- Example scenario: composite index conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
