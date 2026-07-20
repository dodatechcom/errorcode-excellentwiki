---
title: "[Solution] Azure Cosmos DB Cassandra API Error — table, consistency, and query failures"
description: "Fix Azure Cosmos DB Cassandra API error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 131
---

Cosmos DB Cassandra API errors involve table schema mismatches, consistency level conflicts, or CQL query failures during read/write operations.

## Common Causes
- CQL command syntax not supported by Cassandra API compatibility layer
- Table schema change not propagated across all replicas
- Consistency level set too high causing latency spikes
- Column type mismatch between driver and Cosmos table definition
- Keyspace replication factor exceeding physical region count

## How to Fix
### Check Cassandra keyspace
```bash
az cosmosdb cassandra keyspace show \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --name myKeyspace
```

### Update keyspace throughput
```bash
az cosmosdb cassandra keyspace update \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --name myKeyspace \
  --max-throughput 8000
```

### Create Cassandra table
```bash
az cosmosdb cassandra table create \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --keyspace-name myKeyspace \
  --name myTable \
  --partition-key "pk" \
  --schema '[{"name":"pk","type":"utf8"},{"name":"id","type":"uuid"}]' \
  --default-ttl 86400
```

### Update table TTL
```bash
az cosmosdb cassandra table update \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --keyspace-name myKeyspace \
  --name myTable \
  --default-ttl 172800
```

## Examples
### List Cassandra tables
```bash
az cosmosdb cassandra table list \
  --resource-group myResourceGroup \
  --account-name myCosmosAccount \
  --keyspace-name myKeyspace
```

### Check Cassandra API metrics
```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.DocumentDB/databaseAccounts/myCosmosAccount \
  --metric "CassandraRequests"
```

## Related Errors
- {{< relref "/cloud/azure/azure-cosmos-error" >}}
- {{< relref "/cloud/azure/azure-cosmos-mongo-error" >}}
- {{< relref "/cloud/azure/azure-cosmos-gremlin-error" >}}
