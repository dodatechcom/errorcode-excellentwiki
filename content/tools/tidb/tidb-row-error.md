---
title: "[Solution] TiDB Row Error — How to Fix"
description: "Fix TiDB row errors by resolving row size limits, fixing row format mismatches, and handling row-level lock conflicts in DML operations"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Row Error

TiDB row errors occur when row operations exceed size limits, encounter format issues, or fail due to row-level conflicts during DML operations.

## Why It Happens

- Row data exceeds the maximum row size limit
- Row contains more columns than the table definition allows
- BLOB or TEXT column data is too large for the configured row format
- Row format (COMPACT vs DYNAMIC) is not supported by the storage engine
- Insert or update violates row-level uniqueness constraints
- Row encoding fails for complex data types

## Common Error Messages

```
ERROR: Row size too large
```

```
ERROR: too many columns for table
```

```
ERROR: column data too long
```

```
ERROR: duplicate key error on update
```

## How to Fix It

### 1. Fix Row Size Issues

```sql
-- Check table row size
SELECT
  table_name,
  ROUND(data_length / rows, 0) AS avg_row_bytes
FROM information_schema.tables
WHERE table_schema = 'mydb'
ORDER BY data_length DESC;

-- Reduce row size by splitting into separate tables
CREATE TABLE orders_metadata (
  order_id INT PRIMARY KEY,
  description TEXT
);

-- Use TEXT type for large values (stored off-page)
ALTER TABLE my_table MODIFY notes TEXT;
```

### 2. Fix Column Count Issues

```sql
-- Check current column count
SELECT COUNT(*) AS column_count
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'mydb' AND TABLE_NAME = 'my_table';

-- TiDB supports up to 512 columns per table
-- If you need more, normalize the schema
CREATE TABLE my_table_ext (
  id INT PRIMARY KEY,
  extra_json JSON
);
```

### 3. Fix Row Format Issues

```sql
-- Set row format
ALTER TABLE my_table ROW_FORMAT = DYNAMIC;

-- Check current row format
SELECT TABLE_NAME, ROW_FORMAT
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'mydb';
```

### 4. Fix Row Lock Conflicts

```sql
-- Check for locked rows
SELECT * FROM information_schema.INNODB_LOCK_WAITS;

-- Use optimistic transaction to reduce conflicts
SET tidb_txn_mode = 'optimistic';

-- Retry on duplicate key error
-- Application-level retry logic
```

## Common Scenarios

- **Insert fails with row too large**: Use TEXT/BLOB or split data into a related table.
- **UPDATE fails with row size limit**: Check for oversized VARCHAR or BLOB columns.
- **Too many columns error**: Normalize the schema to reduce column count.

## Prevent It

- Design tables with row size in mind from the start
- Use TEXT/BLOB for large values and avoid them in indexes
- Monitor row sizes on growing tables

## Related Pages

- [TiDB DML Error](/tools/tidb/tidb-dml-error)
- [TiDB Table Partition Error](/tools/tidb/tidb-table-partition-error)
- [TiDB Index Error](/tools/tidb/tidb-index-error)
