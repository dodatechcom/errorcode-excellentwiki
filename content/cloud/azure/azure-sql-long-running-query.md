---
title: "[Solution] Azure SQL Long Running Query Error"
description: "Identify and fix long-running queries causing performance degradation in Azure SQL Database."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Long-running queries consume excessive resources and block other operations. This degrades overall database performance and can cause timeout errors.

## Common Causes

- Missing indexes force full table scans on large datasets
- Query optimizer chooses an inefficient execution plan
- Statistics are outdated and the optimizer makes poor decisions
- Large result sets are returned without pagination

## How to Fix

### Find long-running queries

```sql
SELECT TOP 10
    qs.total_elapsed_time / qs.execution_count AS avg_elapsed_time,
    qs.execution_count,
    SUBSTRING(qt.text, (qs.statement_start_offset/2)+1, 
        ((CASE qs.statement_end_offset
            WHEN -1 THEN DATALENGTH(qt.text)
            ELSE qs.statement_end_offset
        END - qs.statement_start_offset)/2)+1) AS query_text
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) qt
ORDER BY avg_elapsed_time DESC;
```

### Update statistics

```sql
UPDATE STATISTICS myTable WITH FULLSCAN;
```

### Add missing index

```sql
CREATE INDEX IX_myTable_column 
ON myTable (column1, column2) 
INCLUDE (column3);
```

### Kill blocking queries

```sql
SELECT * FROM sys.dm_exec_requests WHERE blocking_session_id <> 0;
KILL <session_id>;
```

## Examples

- Query takes 30 seconds to complete instead of milliseconds due to missing index
- Statistics on a 100M row table are 6 months old causing full scans
- UPDATE statement holds exclusive lock for 5 minutes blocking all reads

## Related Errors

- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error" >}}) -- General SQL errors.
- [Azure SQL Connection Throttled]({{< relref "/cloud/azure/azure-sql-connection-throttled" >}}) -- Throttling issues.
