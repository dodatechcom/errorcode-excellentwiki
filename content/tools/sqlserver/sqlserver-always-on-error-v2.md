---
title: "SQL Server Always On - availability group error"
description: "SQL Server Always On availability group fails to synchronize or perform failover between replicas"
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

An Always On availability group error occurs when the high-availability features of SQL Server fail to maintain synchronized replicas or perform failover operations. This can impact database availability and disaster recovery capabilities.

## Common Causes

- Secondary replica falling behind in log send queue
- Network connectivity loss between replicas
- Listener DNS resolution failure
- Log send queue growing too large
- Replica suspension or error state

## How to Fix

1. Check availability group health:

```sql
SELECT
  ag.name AS ag_name,
  ar.replica_server_name,
  ars.role_desc,
  ars.synchronization_health_desc,
  ars.connected_state_desc
FROM sys.availability_groups ag
JOIN sys.availability_replicas ar ON ag.group_id = ar.group_id
JOIN sys.dm_hadr_availability_replica_states ars ON ar.replica_id = ars.replica_id;
```

2. Check log send queue:

```sql
SELECT
  ag.name,
  ar.replica_server_name,
  ars.log_send_queue_size,
  ars.redo_queue_size
FROM sys.availability_groups ag
JOIN sys.availability_replicas ar ON ag.group_id = ar.group_id
JOIN sys.dm_hadr_availability_replica_states ars ON ar.replica_id = ars.replica_id;
```

3. Resume a suspended replica:

```sql
ALTER DATABASE mydb SET HADR RESUME;
```

4. Check for failed log send:

```sql
SELECT
  database_name,
  last_commit_time,
  last_hardened_lsn,
  last_redone_lsn
FROM sys.dm_hadr_database_replica_states;
```

5. Force manual failover:

```sql
-- On primary
ALTER AVAILABILITY GROUP myag FORCE_FAILOVER_ALLOW_DATA_LOSS;
```

6. Repair log send issues:

```bash
# Re-initialize log shipping
# On secondary: restore full backup
RESTORE DATABASE mydb FROM DISK = '/backup/mydb.bak'
WITH NORECOVERY;
-- Then re-add to availability group
```

## Examples

```sql
-- Error: The availability group database "mydb" is not healthy
SELECT synchronization_health_desc
FROM sys.dm_hadr_availability_replica_states
WHERE is_local = 1;
-- Results: NOT_HEALTHY

-- Check specific issue
SELECT last_hardened_lsn, last_redone_lsn
FROM sys.dm_hadr_database_replica_states
WHERE database_id = DB_ID('mydb');
```

## Related Errors

- [Replication error]({{< relref "/tools/sqlserver/sqlserver-replication-error" >}})
- [Connection error]({{< relref "/tools/sqlserver/sqlserver-connection-error" >}})
