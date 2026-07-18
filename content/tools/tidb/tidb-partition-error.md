---
title: "[Solution] TiDB Partition Error — How to Fix"
description: "Fix TiDB partition errors by resolving table partition failures, fixing partition pruning issues, and handling partition management problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Partition Error

TiDB partition errors occur when creating, querying, or managing partitioned tables. TiDB supports RANGE, LIST, and HASH partitioning.

## Why It Happens

- Partition key is not in primary key
- Partition definition has overlapping ranges
- Partition pruning is not working
- Too many partitions degrade performance
- Partition operation is not supported
- Partition key type is not supported

## Common Error Messages

```
ERROR: partition key not in primary key
```

```
ERROR: overlapping partition ranges
```

```
ERROR: too many partitions
```

```
ERROR: partition pruning failed
```

## How to Fix It

### 1. Create Partitioned Table

```sql
-- RANGE partitioning
CREATE TABLE orders (
  id INT NOT NULL,
  created_at DATE NOT NULL,
  amount DECIMAL
) PARTITION BY RANGE (YEAR(created_at)) (
  PARTITION p2022 VALUES LESS THAN (2023),
  PARTITION p2023 VALUES LESS THAN (2024),
  PARTITION p2024 VALUES LESS THAN (2025)
);

-- HASH partitioning
CREATE TABLE users (
  id INT NOT NULL,
  name VARCHAR(100)
) PARTITION BY HASH(id) PARTITIONS 8;

-- LIST partitioning
CREATE TABLE regions (
  id INT NOT NULL,
  region VARCHAR(50)
) PARTITION BY LIST COLUMNS(region) (
  PARTITION p_us VALUES IN ('us-east', 'us-west'),
  PARTITION p_eu VALUES IN ('eu-west', 'eu-central')
);
```

### 2. Fix Partition Pruning

```sql
-- Ensure queries include partition key for pruning
EXPLAIN SELECT * FROM orders WHERE YEAR(created_at) = 2024;

-- Bad: no pruning
SELECT * FROM orders WHERE amount > 100;

-- Good: pruning works
SELECT * FROM orders WHERE YEAR(created_at) = 2024 AND amount > 100;
```

### 3. Manage Partitions

```sql
-- Add partition
ALTER TABLE orders ADD PARTITION (
  PARTITION p2025 VALUES LESS THAN (2026)
);

-- Drop partition
ALTER TABLE orders DROP PARTITION p2022;

-- Check partition info
SHOW CREATE TABLE orders;
SELECT * FROM information_schema.partitions WHERE table_name = 'orders';
```

### 4. Optimize Partition Performance

```sql
-- Use appropriate number of partitions
-- Too many partitions degrade performance
-- Recommended: less than 1000 partitions per table

-- Check partition count
SELECT COUNT(*) FROM information_schema.partitions
WHERE table_name = 'orders';
```

## Common Scenarios

- **Partition pruning not working**: Ensure WHERE clause includes partition key.
- **Too many partitions**: Reduce partition count or use larger time ranges.
- **Partition key not in PK**: Include partition key in primary key definition.

## Prevent It

- Design partition strategy before creating tables
- Keep partition count reasonable (<1000)
- Always include partition key in WHERE clauses

## Related Pages

- [TiDB Placement Error](/tools/tidb/tidb-placement-error)
- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
- [TiDB Query Error](/tools/tidb/tidb-query-error)
