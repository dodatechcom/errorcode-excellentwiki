---
title: "[Solution] Azure Cosmos DB MongoDB API Error — index, throughput, and connection failures"
description: "Fix Azure Cosmos DB MongoDB API error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 130
---

Cosmos DB MongoDB API errors involve index creation failures, RU consumption exceeding provisioned throughput, or wire protocol compatibility issues.

## Common Causes
- Index policy not configured causing full collection scans
- Request unit consumption exceeding autoscale max threshold
- MongoDB driver version incompatible with Cosmos wire protocol
- Sharded collection shard key distribution causing hot partitions
- Cross-partition queries degrading performance without proper indexes

## How to Fix
### Check database RU consumption
```bash
az cosmosdb sql database show \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --name myDatabase \
  --query "resource"
```

### Update autoscale RU
```bash
az cosmosdb mongodb database update \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --name myDatabase \
  --max-throughput 10000
```

### Create MongoDB index
```bash
az cosmosdb mongodb collection update \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --database-name myDatabase \
  --name myCollection \
  --idx "[{\"key\":{\"_id\":1}}]"
```

### List partition key usage
```bash
az cosmosdb show \
  --resource-group myResourceGroup \
  --name myCosmosAccount \
  --query "locations"
```

## Examples
### Create MongoDB collection with autoscale
```bash
az cosmosdb mongodb collection create \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --database-name myDatabase \
  --name myCollection \
  --shard "_id" \
  --max-throughput 5000
```

### Query Mongo metrics
```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.DocumentDB/databaseAccounts/myCosmosAccount \
  --metric "MongoRequests,normalizedRUConsumption"
```

## Related Errors
- {{< relref "/cloud/azure/azure-cosmos-error" >}}
- {{< relref "/cloud/azure/azure-cosmos-cassandra-error" >}}
- {{< relref "/cloud/azure/azure-postgresql-error" >}}
