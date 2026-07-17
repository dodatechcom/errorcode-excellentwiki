---
title: "SQL Server Always On Error"
description: "SQL Server Always On Availability Groups encounter errors during failover or synchronization."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# SQL Server Always On Error

A SQL Server Always On error occurs when the Availability Group encounters issues with failover, synchronization, or listener configuration. Always On provides high availability and disaster recovery.

## Common Causes

- Secondary replica synchronization issues
- Listener DNS resolution failure
- Quorum loss
- Network connectivity between replicas
- Database not in AG

## How to Fix

### Check AG Status

```sql
SELECT ag.name, ars.role_desc, ars.synchronization_health_desc
FROM sys.availability_groups ag
JOIN sys.dm_hadr_availability_replica_states ars ON ag.group_id = ars.group_id;
```

### Check Database Synchronization

```sql
SELECT db.name, drs.synchronization_state_desc, drs.last_commit_time
FROM sys.dm_hadr_database_replica_states drs
JOIN sys.databases db ON drs.database_id = db.database_id;
```

### Check Listener

```sql
SELECT listener_id, dns_name, port
FROM sys.availability_group_listeners;
```

### Force Failover

```sql
-- On secondary
ALTER AVAILABILITY GROUP myag FORCE_FAILOVER_ALLOW_DATA_LOSS;
```

### Check Quorum

```sql
SELECT * FROM sys.dm_hadr_cluster_members;
```

### Fix Synchronization

```sql
-- Resume data movement
ALTER DATABASE mydb SET HADR RESUME;
```

### Check Network Connectivity

```bash
# Between replicas
telnet replica2 5022
```

## Examples

```sql
-- Check AG health
SELECT ag.name, ars.role_desc, ars.synchronized_desc
FROM sys.availability_groups ag
JOIN sys.dm_hadr_availability_replica_states ars ON ag.group_id = ars.group_id;
-- Secondary shows NOT_SYNCHRONIZING
```

## Related Errors

- [Replication Error]({{< relref "/tools/sqlserver/sqlserver-replication-error" >}}) — replication issues
- [Connection Error]({{< relref "/tools/sqlserver/sqlserver-connection-error" >}}) — connection failure
