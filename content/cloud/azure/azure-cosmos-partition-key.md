---
title: "[Solution] Azure Cosmos DB Partition Key Error"
description: "Fix Azure Cosmos DB partition key design issues causing hot partitions and throttling."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Partition key errors occur when the chosen partition key creates uneven data distribution. This leads to hot partitions, throttling, and poor query performance.

## Common Causes

- Partition key has low cardinality (e.g., boolean or status field with few values)
- High-traffic data is concentrated in a single partition
- Partition key was chosen without analyzing the access pattern
- Existing collection cannot change its partition key without migration

## How to Fix

### Review current partition key distribution

```bash
az cosmosdb sql container show \
  --account-name myCosmosDB \
  --database-name myDB \
  --name myContainer \
  --query "partitionKey"
```

### Monitor partition distribution

```bash
az cosmosdb metrics list \
  --name "Logical Partition Size" \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.DocumentDB/databaseAccounts/myCosmosDB
```

### Create a new container with a better partition key

```bash
az cosmosdb sql container create \
  --account-name myCosmosDB \
  --database-name myDB \
  --name myNewContainer \
  --partition-key-path "/tenantId" \
  --throughput 4000
```

### Migrate data with a new partition key

```bash
az cosmosdb data-transfer create \
  --source-account myCosmosDB \
  --dest-account myCosmosDB \
  --source-database myDB \
  --dest-database myDB \
  --source-container oldContainer \
  --dest-container newContainer
```

## Examples

- Container uses `/status` partition key where 90% of items have the same status value
- Partition key `/country` causes hot partition when most traffic comes from one country
- Changing from `/id` to `/userId` improves query performance by 5x with better distribution

## Related Errors

- [Azure Cosmos Throttling]({{< relref "/cloud/azure/azure-cosmos-throttling" >}}) -- Throttling issues.
- [Azure Cosmos RU Limit]({{< relref "/cloud/azure/azure-cosmos-ru-limit" >}}) -- RU limit issues.
