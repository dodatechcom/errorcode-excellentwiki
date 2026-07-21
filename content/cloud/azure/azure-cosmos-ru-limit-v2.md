---
title: "[Solution] AZURE Cosmos RU Limit"
description: "CosmosRUExceeded for request units."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cosmos RU Limit` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- RU/s limit hit for container
- Partition hot key skew

## How to Fix

### Check throughput

```bash
az cosmosdb sql container throughput show -a myAccount -d myDB -n myContainer
```

## Examples

- Example scenario: ru/s limit hit for container
- Example scenario: partition hot key skew

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
