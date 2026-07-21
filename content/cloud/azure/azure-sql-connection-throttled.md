---
title: "[Solution] Azure SQL Database Connection Throttled"
description: "Fix Azure SQL Database connection throttling errors caused by resource limits and connection pool exhaustion."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Connection throttling occurs when Azure SQL Database reaches its resource governance limits. This causes new connections to be rejected or timed out.

## Common Causes

- Too many concurrent connections exceed the DTU or vCore limit
- Connection pool is not properly managed and connections are leaking
- Long-running transactions hold locks and block new connections
- Database is in the Basic tier with very low resource limits

## How to Fix

### Check current resource usage

```bash
az sql db show \
  --name myDB \
  --server myServer \
  --resource-group myRG \
  --query "currentServiceObjectiveName"
```

### Monitor resource governance

```sql
SELECT 
    db_name() as database_name,
    request_id,
    request_type,
    session_id,
    total_cpu_time_ms,
    total_duration_ms
FROM sys.dm_db_requests
WHERE total_cpu_time_ms > 1000
ORDER BY total_cpu_time_ms DESC;
```

### Scale up the database tier

```bash
az sql db update \
  --name myDB \
  --server myServer \
  --resource-group myRG \
  --service-tier GeneralPurpose \
  --capacity 4
```

### Kill long-running queries

```sql
SELECT session_id, command, start_time, total_elapsed_time
FROM sys.dm_exec_requests
WHERE total_elapsed_time > 300000;
```

## Examples

- Application receives `AzureSQLDatabaseThrottled` error during peak usage hours
- Connection pool exhaustion causes `TimeoutException` in .NET applications
- Database throttles at 400 DTUs despite showing 200 DTU usage in metrics

## Related Errors

- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error" >}}) -- General SQL errors.
- [Azure DTU Exhausted]({{< relref "/cloud/azure/azure-dtu-exhausted" >}}) -- DTU limit issues.
