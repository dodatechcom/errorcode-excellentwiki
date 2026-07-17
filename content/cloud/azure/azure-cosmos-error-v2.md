---
title: "[Solution] Azure Cosmos DB — request rate too large"
description: "Fix Azure Cosmos DB request rate too large. Resolve Cosmos DB throttling and RU issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Cosmos DB request rate too large error means the request exceeded the provisioned Request Units (RU/s) for the container or database. Cosmos DB throttles requests that exceed the allocated throughput with HTTP 429 status.

## What This Error Means

Cosmos DB measures all operations in Request Units (RUs). Each operation consumes RUs based on data size, index complexity, and consistency level. When total RU consumption exceeds the provisioned RU/s, Cosmos DB returns HTTP 429 (`Request Rate Too Large`) with a `x-ms-retry-after-ms` header indicating when to retry. This throttling protects the database from overload and ensures predictable performance for all tenants.

## Common Causes

- Provisioned RU/s too low for the workload
- Hot partition key causing uneven RU distribution
- Large point reads or queries consuming more RUs than expected
- Missing or excessive indexing consuming write RUs
- Bulk operations exceeding container throughput
- Cross-partition queries consuming RUs from all partitions

## How to Fix

### Check Current Throughput

```bash
az cosmosdb sql container show \
  --account-name my-account \
  --database-name my-db \
  --name my-container \
  --query 'resource.resourceThroughput'
```

### Monitor RU Consumption

```bash
az monitor metrics list \
  --resource my-cosmos-account \
  --resource-group my-rg \
  --metric NormalizedRUConsumption \
  --aggregation Average
```

### Increase Provisioned Throughput

```bash
az cosmosdb sql container update \
  --account-name my-account \
  --database-name my-db \
  --name my-container \
  --max-throughput 10000
```

### Enable Autoscale

```bash
az cosmosdb sql container update \
  --account-name my-account \
  --database-name my-db \
  --name my-container \
  --max-throughput 10000
```

### Optimize Queries

```sql
-- Use point reads instead of queries
-- Point read: 1 RU
-- Query: varies based on data scanned

-- Use partition key in queries
SELECT * FROM c WHERE c.partitionKey = 'value' AND c.id = '123'
```

### Reduce Indexing Overhead

```json
{
  "indexingPolicy": {
    "includedPaths": [
      { "path": "/name/?" }
    ],
    "excludedPaths": [
      { "path": "/*" }
    ]
  }
}
```

### Implement Retry Logic

```python
import time
from azure.cosmos.exceptions import HttpResponseError

try:
    container.create_item(body=document)
except HttpResponseError as e:
    if e.status_code == 429:
        retry_after = e.headers.get('x-ms-retry-after-ms', 1000)
        time.sleep(int(retry_after) / 1000)
        container.create_item(body=document)
```

## Related Errors

- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error-v2" >}}) — authentication failed
- [AWS DynamoDB Error]({{< relref "/cloud/aws/aws-dynamodb-error-v2" >}}) — throughput exceeded
- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error-v2" >}}) — firewall blocked
