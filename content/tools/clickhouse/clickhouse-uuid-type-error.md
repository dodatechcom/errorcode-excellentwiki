---
title: "[Solution] ClickHouse UUID Type Error"
description: "Fix ClickHouse UUID type errors when inserting or comparing UUID values"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse UUID Type Error

UUID type errors occur when ClickHouse cannot parse or handle UUID values correctly.

## Common Causes

- UUID string not in standard format
- Comparing UUID with String directly
- UUID column used in ORDER BY without index
- Generating duplicate UUIDs

## How to Fix

Parse UUID string:

```sql
SELECT toUUID('123e4567-e89b-12d3-a456-426614174000') AS id;
```

Generate UUID:

```sql
SELECT generateUUIDv4() AS new_uuid;
```

Create table with UUID:

```sql
CREATE TABLE t (id UUID DEFAULT generateUUIDv4()) ENGINE = MergeTree() ORDER BY id;
```

## Examples

```sql
SELECT id, UUIDNumToString(id) AS id_str FROM my_table LIMIT 5;
```
