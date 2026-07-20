---
title: "[Solution] Azure Cosmos DB Table API Error — partition, entity, and throttle failures"
description: "Fix Azure Cosmos DB Table API error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 133
---

Cosmos DB Table API errors involve partition key hot-spots, entity batch operation failures, or request throttling that impacts table storage workloads.

## Common Causes
- Partition key distribution causing hot partition during high writes
- Batch operations exceeding 100 entity limit per transaction
- RU consumption exceeding provisioned throughput during bulk imports
- Entity ETag conflicts during concurrent update operations
- Cross-partition queries not using proper partition filters

## How to Fix
### Check table RU consumption
```bash
az cosmosdb sql table show \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --name myTable \
  --query "resource"
```

### Update table throughput
```bash
az cosmosdb sql table update \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --name myTable \
  --max-throughput 10000
```

### Create SQL table with partition key
```bash
az cosmosdb sql table create \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --name myTable \
  --partition-key-path "/pk" \
  --max-throughput 4000
```

### List table containers
```bash
az cosmosdb sql table list \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount
```

## Examples
### Create table API account
```bash
az cosmosdb create \
  --resource-group myResourceGroup \
  --name myCosmosAccount \
  --kind GlobalDocumentDB \
  --capabilities EnableTable
```

### Query table metrics
```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.DocumentDB/databaseAccounts/myCosmosAccount \
  --metric "TableRequests"
```

## Related Errors
- {{< relref "/cloud/azure/azure-cosmos-error" >}}
- {{< relref "/cloud/azure/azure-storage-table-error" >}}
- {{< relref "/cloud/azure/azure-storage-error" >}}
