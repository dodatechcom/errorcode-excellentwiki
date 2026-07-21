---
title: "[Solution] ClickHouse Low Cardinality Error"
description: "Fix ClickHouse LowCardinality errors when dictionary encoding fails for string columns"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse LowCardinality Error

LowCardinality errors occur when the dictionary encoding cannot handle the column data efficiently.

## Common Causes

- Too many unique values exceeding dictionary limit
- Mixing LowCardinality with Nullable
- Column values growing after initial insert
- Dictionary overflow on high-cardinality columns

## How to Fix

Check cardinality:

```sql
SELECT uniq(column) AS cardinality FROM my_table;
```

Use LowCardinality correctly:

```sql
-- GOOD: LowCardinality(String) for columns with few distinct values
CREATE TABLE t (status LowCardinality(String)) ENGINE = MergeTree() ORDER BY status;
```

Avoid Nullable with LowCardinality:

```sql
-- BAD
CREATE TABLE t (col Nullable(LowCardinality(String)));
-- GOOD: use default value instead
CREATE TABLE t (col LowCardinality(String) DEFAULT '');
```

## Examples

```sql
SELECT status, count() FROM my_table GROUP BY status;
```
