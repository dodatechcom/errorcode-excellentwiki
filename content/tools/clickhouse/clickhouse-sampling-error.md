---
title: "[Solution] ClickHouse Sampling Error"
description: "Fix ClickHouse sampling errors when TABLESAMPLE queries produce incorrect results"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Sampling Error

Sampling errors occur when TABLESAMPLE queries fail or produce statistically invalid results.

## Common Causes

- Sampling key not defined on table
- Sample percentage too small for meaningful results
- Sampling on non-numeric column
- Using sampling with FINAL keyword

## How to Fix

Define table with sampling key:

```sql
CREATE TABLE sampled_table (id UInt64, name String)
ENGINE = MergeTree() SAMPLE BY id ORDER BY id;
```

Use sampling:

```sql
SELECT * FROM sampled_table SAMPLE 0.1;
```

Check sampling key:

```sql
SELECT name, sampling_key FROM system.tables WHERE name = 'sampled_table';
```

## Examples

```sql
SELECT count() FROM sampled_table SAMPLE 0.01;
```
