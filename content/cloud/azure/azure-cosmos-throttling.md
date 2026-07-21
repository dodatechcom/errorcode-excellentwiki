---
title: "[Solution] Azure Cosmos DB Throttling Error (429)"
description: "Fix Azure Cosmos DB request rate throttling with RU optimization and retry strategies."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Cosmos DB returns HTTP 429 (Too Many Requests) when request units are exhausted. This causes latency spikes and failed operations in applications.

## Common Causes

- Provisioned request units are too low for the workload pattern
- Hot partition key leads to uneven RU consumption across partitions
- Large item reads or cross-partition queries consume more RU than expected
- Bulk operations do not implement proper retry-after headers

## How to Fix

### Check current RU consumption

```bash
az cosmosdb show \
  --name myCosmosDB \
  --resource-group myRG \
  --query "databaseAccountOfferType"
```

### Scale RU throughput

```bash
az cosmosdb sql database update \
  --account-name myCosmosDB \
  --resource-group myRG \
  --name myDatabase \
  --max-throughput 10000
```

### Monitor request rate statistics

```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.DocumentDB/databaseAccounts/myCosmosDB \
  --metric "TotalRequestUnits"
```

### Implement retry logic in code

```csharp
var response = await container.ReadItemAsync<MyItem>(
    partitionKey: new PartitionKey("pk"),
    id: "itemId",
    requestOptions: new ItemRequestOptions
    {
        EnableContentResponseOnWrite = false
    });
```

## Examples

- Application receives `RequestRateTooLarge` errors during peak traffic
- RU consumption spikes to 100% when a single partition receives all writes
- Cross-partition query consumes 5x more RU than point reads on the same item

## Related Errors

- [Azure Cosmos DB Error]({{< relref "/cloud/azure/azure-cosmos-error" >}}) -- General Cosmos DB errors.
- [Azure Cosmos RU Limit]({{< relref "/cloud/azure/azure-cosmos-ru-limit" >}}) -- RU limit issues.
