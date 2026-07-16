---
title: "Azure CosmosDB: Request Rate Is Too Large"
description: "CosmosDB: Request rate is too large — Fix Azure Cosmos DB throttling errors (429)."
cloud: ["azure"]
error-types: ["quota-error"]
severities: ["error"]
tags: ["azure", "cosmosdb", "cosmos", "throttling", "429", "request-rate", "ru"]
weight: 5
---

The `Request rate is too large` error (HTTP 429) occurs when an Azure Cosmos DB account receives more requests per second than its provisioned Request Units (RU) allow. Cosmos DB throttles requests when throughput is exceeded.

## Common Causes

- Provisioned RU/s is too low for the workload
- Hot partition key causes uneven RU consumption
- Large document reads/writes consume more RU than expected
- No retry logic with exponential backoff for transient 429 errors

## How to Fix

Check current throughput:

```bash
az cosmosdb show \
  --name my-cosmosdb \
  --resource-group my-rg \
  --query '{Name:name, ProvisionedThroughput:resourceGroup}'
```

Scale up the RU/s:

```bash
az cosmosdb sql database update \
  --account-name my-cosmosdb \
  --name my-db \
  --resource-group my-rg \
  --max-throughput 10000
```

Enable autoscale:

```bash
az cosmosdb sql database create \
  --account-name my-cosmosdb \
  --name my-db \
  --resource-group my-rg \
  --max-throughput 4000
```

Implement retry logic:

```csharp
// C# example with retry policy
var options = new RequestOptions
{
    MaxRetryAttemptsOnRateLimitedRequests = 10,
    MaxRetryWaitTimeOnRateLimitedRequests = TimeSpan.FromSeconds(10)
};
var response = await client.ReadDocumentAsync(uri, options);
```

## Examples

- Bulk insert operation consumes 5000 RU/s but the account is provisioned for 4000 RU/s
- A single partition key receives all writes, causing hot partition throttling
- Point reads on large documents (1MB+) consume more RU than expected

## Related Errors

- [Azure Quota Exceeded]({{< relref "/cloud/azure/quota-exceeded" >}}) — subscription quota limits.
- [AWS Throttling]({{< relref "/cloud/aws/throttling" >}}) — AWS API throttling.
- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded2" >}}) — GCP equivalent.
