---
title: "[Solution] TiDB Sequence Error — How to Fix"
description: "Fix TiDB sequence errors by resolving auto-increment issues, fixing sequence cache problems, and handling ID allocation failures"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Sequence Error

TiDB sequence errors occur when using AUTO_INCREMENT, sequences, or other ID generation mechanisms in a distributed environment.

## Why It Happens

- AUTO_INCREMENT is exhausted
- Sequence cache is too small
- AUTO_RANDOM conflicts with AUTO_INCREMENT
- ID allocation rate exceeds cache refill rate
- Sequence increment is not positive
- Multiple TiDB servers allocate IDs concurrently

## Common Error Messages

```
ERROR: AUTO_INCREMENT value exhausted
```

```
ERROR: sequence cache empty
```

```
ERROR: duplicate entry for key
```

```
ERROR: invalid sequence increment
```

## How to Fix It

### 1. Use AUTO_INCREMENT Correctly

```sql
-- Standard AUTO_INCREMENT
CREATE TABLE users (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)
);

-- Check current AUTO_INCREMENT value
SHOW CREATE TABLE users;

-- Reset AUTO_INCREMENT (caution)
ALTER TABLE users AUTO_INCREMENT = 1;
```

### 2. Use Sequences

```sql
-- Create sequence
CREATE SEQUENCE order_seq START 1 INCREMENT 1 CACHE 100;

-- Use in table
CREATE TABLE orders (
  id BIGINT DEFAULT nextval('order_seq') PRIMARY KEY,
  amount DECIMAL
);

-- Check sequence value
SELECT lastval('order_seq');
SELECT currval('order_seq');
```

### 3. Use AUTO_RANDOM for Write-Heavy Tables

```sql
-- AUTO_RANDOM avoids AUTO_INCREMENT bottlenecks
CREATE TABLE events (
  id BIGINT AUTO_RANDOM PRIMARY KEY,
  data JSONB
);

-- AUTO_RANDOM distributes IDs across regions
-- Avoids hotspot on single region
```

### 4. Monitor ID Usage

```sql
-- Check AUTO_INCREMENT value
SHOW CREATE TABLE users;

-- Check sequence value
SELECT * FROM information_schema.sequences WHERE sequence_name = 'order_seq';

-- Monitor region hotspot
curl http://pd1:2379/pd/api/v1/regions/hot
```

## Common Scenarios

- **AUTO_INCREMENT hotspot**: Use AUTO_RANDOM for write-heavy tables.
- **Sequence cache empty**: Increase cache size for sequence.
- **ID conflict on merge**: Use UUID or AUTO_RANDOM instead of AUTO_INCREMENT.

## Prevent It

- Use AUTO_RANDOM for high-write tables
- Choose appropriate sequence cache size
- Monitor ID allocation and hotspot

## Related Pages

- [TiDB Auto Random Error](/tools/tidb/tidb-auto-random-error)
- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
- [TiDB Region Error](/tools/tidb/tidb-region-error)
