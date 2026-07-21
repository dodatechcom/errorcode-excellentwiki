---
title: "[Solution] ClickHouse Enum Error"
description: "Fix ClickHouse enum errors when inserting or comparing enum values"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Enum Error

Enum errors occur when ClickHouse encounters invalid enum values during insertion or comparison.

## Common Causes

- Inserting value not defined in Enum8/Enum16
- Enum value truncated in implicit conversion
- Comparing Enum with string
- Enum definition exceeds 8/16 bit range

## How to Fix

Check enum values:

```sql
SELECT name, type FROM system.columns WHERE table = 'my_table' AND type LIKE 'Enum%';
```

Insert valid enum value:

```sql
INSERT INTO my_table (status) VALUES ('active'); -- must match Enum definition
```

Cast enum to string:

```sql
SELECT CAST(status AS String) AS status_str FROM my_table;
```

## Examples

```sql
CREATE TABLE t (status Enum8('active' = 1, 'inactive' = 2)) ENGINE = MergeTree() ORDER BY status;
```
