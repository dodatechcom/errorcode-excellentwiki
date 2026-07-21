---
title: "[Solution] Azure SQL Database Failover Error"
description: "Resolve Azure SQL Database failover group errors that prevent automatic disaster recovery."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Failover errors prevent Azure SQL Database from switching to a secondary server during outages. This can result in extended downtime when the primary server is unavailable.

## Common Causes

- Failover group is not configured or was recently deleted
- Secondary server is in a different region without geo-replication enabled
- Failover group listener DNS record has not propagated
- Database replication lag is too high and failover cannot complete

## How to Fix

### Check failover group status

```bash
az sql failover-group list \
  --server myServer \
  --resource-group myRG
```

### Create a failover group

```bash
az sql failover-group create \
  --name myFailoverGroup \
  --server myServer \
  --resource-group myRG \
  --partner-server myPartnerServer \
  --add databases myDB
```

### Initiate manual failover

```bash
az sql failover-group set-primary \
  --name myFailoverGroup \
  --server myPartnerServer \
  --resource-group myRG
```

### Check replication status

```sql
SELECT 
    database_name, 
    last_commit_time,
    latency
FROM sys.geo_replication_status
WHERE database_name = 'myDB';
```

## Examples

- Failover group shows secondary as "Not Synchronized" due to replication lag
- Automatic failover does not trigger because the health probe is misconfigured
- DNS listener for the failover group resolves to the old primary after failback

## Related Errors

- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error" >}}) -- General SQL errors.
- [Azure Failover Group]({{< relref "/cloud/azure/azure-failover-group" >}}) -- Failover group issues.
