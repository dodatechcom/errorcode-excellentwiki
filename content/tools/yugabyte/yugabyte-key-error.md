---
title: "[Solution] YugabyteDB Key Error — How to Fix"
description: "Fix YugabyteDB key errors by resolving primary key conflicts, fixing key range issues, and handling hash key distribution problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Key Error

YugabyteDB key errors occur when primary key operations, key range queries, or hash key distribution encounters conflicts or configuration issues.

## Why It Happens

- Primary key constraint is violated by duplicate values
- Key range boundaries overlap between tablets
- Composite key columns have wrong order
- Key column data type is incompatible with sharding
- Key lookup exceeds timeout for large datasets
- Hash key produces uneven distribution across tablets

## Common Error Messages

```
ERROR: duplicate key value violates unique constraint
```

```
ERROR: key range conflict
```

```
ERROR: primary key column cannot be NULL
```

```
ERROR: key lookup timeout
```

## How to Fix It

### 1. Fix Primary Key Conflicts

```sql
-- Check for duplicate keys
SELECT id, COUNT(*)
FROM my_table
GROUP BY id
HAVING COUNT(*) > 1;

-- Remove duplicates
DELETE FROM my_table a
WHERE ctid NOT IN (
  SELECT MIN(ctid)
  FROM my_table b
  WHERE a.id = b.id
);

-- Insert with conflict handling
INSERT INTO my_table (id, name)
VALUES (1, 'test')
ON CONFLICT (id)
DO UPDATE SET name = EXCLUDED.name;
```

### 2. Fix Composite Key Issues

```sql
-- Create table with proper composite key
CREATE TABLE sensor_data (
  device_id INT NOT NULL,
  time TIMESTAMPTZ NOT NULL,
  value NUMERIC(10,2),
  PRIMARY KEY (device_id, time)
);
```

### 3. Fix Key Lookup Issues

```sql
-- Ensure index exists on key columns
CREATE INDEX idx_device_time ON sensor_data (device_id, time);

-- Use key range for efficient lookups
SELECT * FROM sensor_data
WHERE device_id = 1
  AND time > '2024-01-01'::TIMESTAMPTZ
  AND time < '2024-02-01'::TIMESTAMPTZ;
```

### 4. Fix NULL Key Issues

```sql
-- Primary key columns cannot be NULL
-- Use NOT NULL constraint
CREATE TABLE my_table (
  id INT NOT NULL,
  name VARCHAR(100),
  PRIMARY KEY (id)
);
```

## Common Scenarios

- **Duplicate key error**: Check for existing rows before inserting.
- **Key lookup is slow**: Ensure proper indexes exist on key columns.
- **NULL in primary key**: Add NOT NULL constraint to key columns.

## Prevent It

- Design primary keys with good distribution properties
- Use composite keys for range queries
- Monitor key distribution across tablets

## Related Pages

- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB Index Error](/tools/yugabyte/yugabyte-index-error)
- [YugabyteDB Schema Error](/tools/yugabyte/yugabyte-schema-error)
