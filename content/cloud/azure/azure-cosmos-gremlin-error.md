---
title: "[Solution] Azure Cosmos DB Gremlin API Error — graph, query, and vertex failures"
description: "Fix Azure Cosmos DB Gremlin API error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 132
---

Cosmos DB Gremlin API errors occur when graph traversals exceed RU limits, vertex/edge operations fail, or partition key conflicts arise during writes.

## Common Causes
- Gremlin traversal depth exceeding RU budget per request
- Partition key on graph causing cross-partition hotspot
- Vertex degree exceeding limits causing edge creation failures
- Graph schema not matching Gremlin API compatible vertex labels
- Autoscale RU max set too low for complex traversals

## How to Fix
### Check Gremlin graph properties
```bash
az cosmosdb gremlin graph show \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --database-name myDatabase \
  --name myGraph \
  --query "resource"
```

### Update graph throughput
```bash
az cosmosdb gremlin graph update \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --database-name myDatabase \
  --name myGraph \
  --max-throughput 12000
```

### Create Gremlin graph with partition key
```bash
az cosmosdb gremlin graph create \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --database-name myDatabase \
  --name myGraph \
  --partition-key-path "/pk" \
  --default-ttl 0 \
  --max-throughput 4000
```

### Check graph indexing policy
```bash
az cosmosdb gremlin graph show \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --database-name myDatabase \
  --name myGraph \
  --query "indexingPolicy"
```

## Examples
### List Gremlin graphs
```bash
az cosmosdb gremlin graph list \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --database-name myDatabase
```

### Create graph database
```bash
az cosmosdb gremlin database create \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --name myDatabase
```

## Related Errors
- {{< relref "/cloud/azure/azure-cosmos-error" >}}
- {{< relref "/cloud/azure/azure-cosmos-table-error" >}}
- {{< relref "/cloud/azure/azure-cosmos-mongo-error" >}}
