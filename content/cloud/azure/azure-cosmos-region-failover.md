---
title: "[Solution] Azure Cosmos DB Region Failover Error"
description: "Resolve Azure Cosmos DB regional failover failures that impact availability and data consistency."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Region failover errors prevent Cosmos DB from failing over to a secondary region during outages. This can cause extended downtime for multi-region deployments.

## Common Causes

- Secondary region does not have sufficient RU provisioned for failover
- Multi-region write is disabled but failover policy expects it
- Consistency level is set to Strong, which requires synchronous replication
- Network latency between regions exceeds the configured threshold

## How to Fix

### Check regional failover status

```bash
az cosmosdb show \
  --name myCosmosDB \
  --resource-group myRG \
  --query "failoverPolicies"
```

### Add a secondary region

```bash
az cosmosdb update \
  --name myCosmosDB \
  --resource-group myRG \
  --locations regionName=eastus2 failoverPriority=1 isZoneRedundant=false
```

### Trigger manual failover

```bash
az cosmosdb failover-priority-change \
  --name myCosmosDB \
  --resource-group myRG \
  --failover-policies eastus2=0 eastus=1
```

### Enable multi-region writes

```bash
az cosmosdb update \
  --name myCosmosDB \
  --resource-group myRG \
  --enable-multiple-write-locations true
```

## Examples

- Failover to secondary region fails because no RU is provisioned there
- Manual failover causes data loss because consistency level is set to Session with single-region writes
- Multi-region write is enabled but some regions have stale data due to replication lag

## Related Errors

- [Azure Cosmos DB Error]({{< relref "/cloud/azure/azure-cosmos-error" >}}) -- General Cosmos DB errors.
- [Azure Cosmos Consistency]({{< relref "/cloud/azure/azure-cosmos-consistency" >}}) -- Consistency issues.
