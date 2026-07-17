---
title: "[Solution] Azure Cosmos DB Error"
description: "Fix Azure Cosmos DB errors. Resolve Cosmos DB connectivity and configuration issues."
cloud: ["azure"]
error-types: ["api-error"]
severities: ["error"]
tags: ["azure", "cosmos", "cosmosdb", "nosql", "database"]
weight: 5
---

An Azure Cosmos DB error occurs when operations on Cosmos DB fail due to connectivity, permission, or configuration issues.

## Common Causes

- Account name or key is incorrect
- Database or container does not exist
- Request unit (RU) throughput exceeded (throttling)
- IP firewall blocking the client
- Partition key value is missing or invalid

## How to Fix

### Check Account Status

```bash
az cosmosdb show --name myaccount --resource-group myRG --query 'documentEndpoint'
```

### Verify Keys

```bash
az cosmosdb keys list --name myaccount --resource-group myRG
```

### Test Connection

```bash
az cosmosdb sql database show --account-name myaccount --resource-group myRG \
  --database-name mydb
```

### Check Throughput

```bash
az cosmosdb sql container show --account-name myaccount --resource-group myRG \
  --database-name mydb --container-name mycontainer \
  --query 'resource.offerThroughput'
```

### Add Firewall Rule

```bash
az cosmosdb network-rule add --resource-group myRG --name myaccount \
  --ip-rule 1.2.3.4
```

## Examples

```bash
# Example 1: Throttling
# Request rate is too large (429)
# Fix: increase RU throughput or optimize queries

# Example 2: Unauthorized
# Invalid credentials for the account
# Fix: use correct master or read-write key
```

## Related Errors

- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error" >}}) — SQL connection error
- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) — Storage error
