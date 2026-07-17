---
title: "SQL Server - replication distribution error"
description: "SQL Server replication fails to distribute changes from publisher to subscriber due to agent or connectivity issues"
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlserver", "replication", "distribution", "agent", "publisher", "subscriber"]
weight: 5
---

A replication distribution error occurs when SQL Server replication agents cannot deliver changes from the publisher through the distributor to the subscribers. This can affect transactional, merge, or snapshot replication.

## Common Causes

- Distribution agent not running or failed
- Network connectivity between publisher and subscriber
- Distribution database corrupted or full
- Subscriber not synchronized for too long
- Agent job schedule misconfigured

## How to Fix

1. Check replication status:

```sql
-- Check distributor status
EXEC sp_replmonitor helppublisher;
EXEC sp_replmonitor helpsubscription;
EXEC sp_replmonitor helpdistributiondb;
```

2. Verify agent jobs are running:

```sql
SELECT name, enabled, date_created, date_modified
FROM msdb.dbo.sysjobs
WHERE name LIKE '%repl%';
```

3. Restart the distribution agent:

```bash
# Command line restart
distrib.exe -Publisher myserver -Subscriber myserver
  -Distributor myserver -DistributorDB distribution
  -PublisherDB mydb -Publication mypub
  -AgentType 10 -Continuous
```

4. Check for errors in agent history:

```sql
SELECT TOP 100
  time, error_id, agent_type, error_text
FROM distribution.dbo.MSdistribution_history
ORDER BY time DESC;
```

5. Reinitialize the subscriber if needed:

```sql
-- Mark subscription for reinitialization
EXEC sp_reinitsubscription
  @subscriber = 'myserver',
  @publication = 'mypub',
  @subscriber_db = 'mydb';
```

6. Check network connectivity between servers:

```bash
sqlcmd -S publisher_server -Q "SELECT 1"
sqlcmd -S subscriber_server -Q "SELECT 1"
```

## Examples

```sql
-- Error: Agent 'myserver-mypub-1' is retrying after a failure
-- Check agent history
SELECT * FROM distribution.dbo.MSdistribution_history
WHERE agent_id = (SELECT id FROM distribution.dbo.MSagents
                   WHERE agent_type = 10 AND publisher_db = 'mydb')
ORDER BY time DESC;
```

## Related Errors

- [Always On error]({{< relref "/tools/sqlserver/sqlserver-always-on-error" >}})
- [Connection error]({{< relref "/tools/sqlserver/sqlserver-connection-error" >}})
