---
title: "SQL Server - full-text index error"
description: "SQL Server full-text index fails to populate, query, or maintain due to configuration or resource issues"
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A full-text index error occurs when SQL Server cannot create, populate, or query a full-text index. This can be caused by missing full-text catalogs, unsupported data types, or resource limitations.

## Common Causes

- Full-text catalog not created or corrupted
- Column type not supported for full-text indexing
- Population process failed or is incomplete
- Full-text filter daemon not running
- Resource constraints during large index population

## How to Fix

1. Check full-text index status:

```sql
SELECT
  t.name AS table_name,
  c.name AS column_name,
  i.is_enabled,
  i.change_tracking_state_desc
FROM sys.fulltext_indexes i
JOIN sys.fulltext_index_columns ic ON i.object_id = ic.object_id
JOIN sys.tables t ON i.object_id = t.object_id
JOIN sys.columns c ON ic.column_id = c.column_id AND ic.object_id = c.object_id;
```

2. Create full-text catalog if missing:

```sql
CREATE FULLTEXT CATALOG ftCatalog AS DEFAULT;
```

3. Enable full-text index on a table:

```sql
CREATE FULLTEXT INDEX ON mytable
  (content_column LANGUAGE English)
  KEY INDEX pk_mytable
  WITH CHANGE_TRACKING AUTO;
```

4. Populate the full-text index:

```sql
-- Full population
ALTER FULLTEXT INDEX ON mytable START FULL POPULATION;

-- Incremental population
ALTER FULLTEXT INDEX ON mytable START INCREMENTAL POPULATION;
```

5. Check full-text daemon status:

```sql
SELECT * FROM sys.dm_fts_active_catalogs;
SELECT * FROM sys.dm_fts_active_datasets;
```

6. Query full-text index:

```sql
-- Use CONTAINS
SELECT * FROM mytable
WHERE CONTAINS(content_column, 'search term');

-- Use FREETEXT
SELECT * FROM mytable
WHERE FREETEXT(content_column, 'search terms');
```

## Examples

```sql
-- Error: Full-text index population failed for table 'mytable'
-- Check population status
SELECT * FROM sys.dm_fts_population_ranges;

-- Restart population
ALTER FULLTEXT INDEX ON mytable STOP POPULATION;
ALTER FULLTEXT INDEX ON mytable START FULL POPULATION;
```

```sql
-- Error: Column 'binary_data' cannot be full-text indexed
CREATE FULLTEXT INDEX ON mytable (binary_data) KEY INDEX pk_mytable;
-- binary_data type is not supported

-- Fix: use a supported column type (VARCHAR, NVARCHAR, VARBINARY, XML)
CREATE FULLTEXT INDEX ON mytable (text_content) KEY INDEX pk_mytable;
```

## Related Errors

- [Index error]({{< relref "/tools/mongodb/mongodb-index-error" >}})
- [Connection error]({{< relref "/tools/sqlserver/sqlserver-connection-error" >}})
