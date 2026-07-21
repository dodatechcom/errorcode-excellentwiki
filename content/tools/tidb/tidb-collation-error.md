---
title: "[Solution] TiDB Collation Error — How to Fix"
description: "Fix TiDB collation errors by resolving charset mismatches, fixing binary comparison issues, and correcting collation configuration"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Collation Error

TiDB collation errors occur when string comparisons or sorting operations fail due to unsupported or mismatched collation settings between columns, tables, or session variables.

## Why It Happens

- Column collation does not match the query collation
- Unsupported collation is specified in the query
- Default collation changed after table creation
- Binary collation used in a non-binary comparison
- Character set and collation are incompatible
- Index collation conflicts with query collation

## Common Error Messages

```
ERROR: Collation 'utf8mb4_0900_ai_ci' is not supported
```

```
ERROR: collation mismatch between binary and non-binary
```

```
ERROR: Unknown collation: 'latin1_swedish_ci'
```

```
ERROR: Column 'name' cannot be resolved: collation mismatch
```

## How to Fix It

### 1. Check Current Collation Settings

```sql
-- Check server default collation
SHOW VARIABLES LIKE 'collation_connection';

-- Check table collation
SHOW CREATE TABLE my_table;

-- Check column collation
SELECT COLUMN_NAME, COLLATION_NAME
FROM information_schema.COLUMNS
WHERE TABLE_NAME = 'my_table';
```

### 2. Fix Collation Mismatch

```sql
-- Alter table collation
ALTER TABLE my_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

-- Alter column collation
ALTER TABLE my_table MODIFY name VARCHAR(255)
  CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Set session collation for the query
SET collation_connection = 'utf8mb4_general_ci';
SELECT * FROM my_table WHERE name = 'hello' COLLATE utf8mb4_general_ci;
```

### 3. Use Compatible Collation

```sql
-- Check supported collations in TiDB
SHOW COLLATION WHERE Charset = 'utf8mb4';

-- Recreate table with supported collation
CREATE TABLE my_table (
  id INT PRIMARY KEY,
  name VARCHAR(255) COLLATE utf8mb4_bin
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
```

### 4. Force Collation in Queries

```sql
-- Use explicit COLLATE clause
SELECT * FROM my_table
WHERE name COLLATE utf8mb4_unicode_ci = 'Hello';

-- Set TiDB specific variables
SET tidb_skip_utf8_check = 0;
SET collation_database = 'utf8mb4_general_ci';
```

## Common Scenarios

- **Import from MySQL 8 defaults**: TiDB does not support `utf8mb4_0900_ai_ci`. Use `utf8mb4_general_ci` instead.
- **Index not used in JOIN**: Ensure collation matches between joined columns so the optimizer can use indexes.
- **Sort order differs from MySQL**: Use the same collation as the source database.

## Prevent It

- Standardize on `utf8mb4_bin` or `utf8mb4_general_ci` across all tables
- Check collation compatibility when migrating from MySQL 8
- Verify collation settings after schema changes

## Related Pages

- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
- [TiDB Index Error](/tools/tidb/tidb-index-error)
- [TiDB Config Error](/tools/tidb/tidb-system-variable-error)
