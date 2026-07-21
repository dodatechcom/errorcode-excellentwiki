---
title: "[Solution] ClickHouse Data Type Error"
description: "Fix ClickHouse data type errors when column types are incompatible with operations"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Data Type Error

Data type errors occur when ClickHouse encounters type incompatibility during query execution.

## Common Causes

- String column used in numeric aggregation
- DateTime compared with Date without cast
- Nullable type on primary key column
- FixedString used where variable length needed

## How to Fix

Check column types:

```sql
SELECT name, type, is_in_primary_key FROM system.columns WHERE table = 'my_table';
```

Cast types:

```sql
SELECT sum(toFloat64(string_column)) FROM my_table;
```

Avoid Nullable on primary key:

```sql
-- BAD
CREATE TABLE t (id Nullable(UInt64)) ENGINE = MergeTree() ORDER BY id;
-- GOOD
CREATE TABLE t (id UInt64) ENGINE = MergeTree() ORDER BY id;
```

## Examples

```sql
SELECT toDate(event_time) AS date, count() FROM events GROUP BY date;
```
