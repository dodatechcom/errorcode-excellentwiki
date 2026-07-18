---
title: "[Solution] ClickHouse UUID Error — How to Fix"
description: "Fix ClickHouse UUID errors including generation failures, type mismatches, and UUID column issues in table definitions"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse UUID Error

UUID errors in ClickHouse occur when using the UUID data type for primary keys, version columns, or unique identifiers. ClickHouse has specific UUID functions and behaviors.

## Why It Happens

- The UUID column is used in a MergeTree primary key without proper ordering
- `generateUUIDv4()` returns the same UUID due to low entropy
- The UUID string format is invalid (not 8-4-4-4-12 hex format)
- UUID is used in JOIN conditions with incompatible types
- The UUID column is part of an ORDER BY that causes excessive parts

## Common Error Messages

```
Code: 46. DB::Exception: UUID function 'generateUUIDv4' is not supported
```

```
Code: 53. DB::Exception: Type mismatch in JOIN: left UUID, right String
```

```
Code: 62. DB::Exception: Invalid UUID format
```

```
Code: 182. DB::Exception: Cannot convert string to UUID
```

## How to Fix It

### 1. Generate UUID Correctly

```sql
-- Generate a UUIDv4
SELECT generateUUIDv4();

-- Use as default in table definition
CREATE TABLE events (
  id UUID DEFAULT generateUUIDv4(),
  name String,
  event_time DateTime
) ENGINE = MergeTree()
ORDER BY (event_time, id);
```

### 2. Fix UUID in Primary Key

```sql
-- BAD: UUID as sole ORDER BY key (random, causes too many parts)
CREATE TABLE events (
  id UUID DEFAULT generateUUIDv4(),
  name String
) ENGINE = MergeTree()
ORDER BY id;

-- GOOD: combine UUID with a monotonic key
CREATE TABLE events (
  id UUID DEFAULT generateUUIDv4(),
  event_time DateTime,
  name String
) ENGINE = MergeTree()
ORDER BY (event_time, id);
```

### 3. Fix UUID Type Mismatch

```sql
-- BAD: comparing UUID to String
SELECT * FROM events WHERE id = '550e8400-e29b-41d4-a716-446655440000';

-- GOOD: cast to UUID type
SELECT * FROM events WHERE id = toUUID('550e8400-e29b-41d4-a716-446655440000');

-- Or use UUID functions
SELECT * FROM events WHERE id = generateUUIDv4();
```

### 4. Query UUID Columns

```sql
-- Extract parts of UUID
SELECT
  id,
  UUIDNumToString(id) AS uuid_str,
  toUInt128(id) AS uuid_num
FROM events;

-- Use UUID in GROUP BY
SELECT id, count() FROM events GROUP BY id;
```

## Common Scenarios

- **Too many parts with UUID primary key**: Add a timestamp column to ORDER BY.
- **UUID comparison fails**: Cast the string to UUID type with `toUUID()`.
- **UUID default not working**: Ensure `generateUUIDv4()` is available in your ClickHouse version.

## Prevent It

- Always combine UUID with a monotonic column (timestamp) in ORDER BY for MergeTree
- Use `toUUID()` to convert string UUIDs before comparison
- Monitor parts count for tables with UUID primary keys

## Related Pages

- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse Type Error](/tools/clickhouse/clickhouse-type-error)
- [ClickHouse Query Error](/tools/clickhouse/clickhouse-query-error)
