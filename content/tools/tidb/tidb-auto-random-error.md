---
title: "[Solution] TiDB Auto Random Error — How to Fix"
description: "Fix TiDB auto random errors by resolving auto_random allocation failures, fixing shard bits configuration, and handling primary key issues"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Auto Random Error

TiDB auto random errors occur when using the AUTO_RANDOM primary key attribute, which distributes data across regions to avoid hotspots.

## Why It Happens

- AUTO_RANDOM is used with non-integer primary key
- Shard bits value is too large for the data volume
- AUTO_RANDOM conflicts with other primary key attributes
- AUTO_RANDOM allocation space is exhausted
- Table is altered to add AUTO_RANDOM after creation
- AUTO_RANDOM interacts poorly with explicit ID insertion

## Common Error Messages

```
ERROR: AUTO_RANDOM is only supported for integer primary key
```

```
ERROR: AUTO_RANDOM shard bits too large
```

```
ERROR: AUTO_RANDOM allocation exhausted
```

```
ERROR: cannot add AUTO_RANDOM to existing table
```

## How to Fix It

### 1. Use AUTO_RANDOM Correctly

```sql
-- Create table with AUTO_RANDOM
CREATE TABLE orders (
  id BIGINT AUTO_RANDOM,
  amount DECIMAL,
  PRIMARY KEY (id)
);

-- With custom shard bits
CREATE TABLE events (
  id BIGINT AUTO_RANDOM(5, 32),  -- 5 shard bits, 32 sign bits
  data JSONB,
  PRIMARY KEY (id)
);
```

### 2. Fix AUTO_RANDOM Issues

```sql
-- Check AUTO_RANDOM status
SHOW CREATE TABLE orders;

-- Remove AUTO_RANDOM if needed
CREATE TABLE orders_new LIKE orders;
ALTER TABLE orders_new DROP PRIMARY KEY, ADD PRIMARY KEY (id);
-- Then migrate data

-- Insert with explicit ID (bypasses AUTO_RANDOM)
SET tidb_allow_auto_random_explicit_insert = 1;
INSERT INTO orders (id, amount) VALUES (1, 100.00);
```

### 3. Configure Shard Bits

```sql
-- Shard bits determine data distribution across regions
-- More shard bits = better distribution but more unique IDs needed

-- Default shard bits: 0
-- Recommended for most workloads: 3-5 shard bits

CREATE TABLE large_table (
  id BIGINT AUTO_RANDOM(5, 32),
  data TEXT,
  PRIMARY KEY (id)
);
```

### 4. Monitor AUTO_RANDOM

```sql
-- Check table schema
SHOW CREATE TABLE orders;

-- Check region distribution
curl http://pd1:2379/pd/api/v1/regions/key/range?startkeys=...&limit=100

-- Monitor hotspot
curl http://pd1:2379/pd/api/v1/regions/hot
```

## Common Scenarios

- **Hotspot on single region**: Use AUTO_RANDOM with appropriate shard bits.
- **AUTO_RANDOM allocation exhausted**: Increase data type size or recreate table.
- **Cannot add AUTO_RANDOM to existing table**: Create new table and migrate data.

## Prevent It

- Use AUTO_RANDOM for write-heavy tables with integer primary keys
- Choose shard bits based on expected data volume
- Monitor region distribution after implementation

## Related Pages

- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
- [TiDB Region Error](/tools/tidb/tidb-region-error)
- [TiDB Split Error](/tools/tidb/tidb-split-error)
