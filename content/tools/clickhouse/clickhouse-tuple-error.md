---
title: "[Solution] ClickHouse Tuple Error"
description: "Fix ClickHouse Tuple type errors when working with composite column types"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Tuple Error

Tuple errors occur when ClickHouse Tuple type operations encounter type mismatches or invalid access patterns.

## Common Causes

- Accessing tuple element with wrong index
- Comparing tuples of different lengths
- Tuple used in hash function incorrectly
- Nested tuple exceeding depth limit

## How to Fix

Access tuple elements:

```sql
SELECT col.1 AS first_elem, col.2 AS second_elem FROM my_table;
```

Create tuple:

```sql
SELECT tuple(a, b) AS composite_key FROM my_table;
```

Compare tuples:

```sql
SELECT * FROM my_table WHERE (a, b) = (1, 'test');
```

## Examples

```sql
SELECT tupleElement(composite, 1) AS elem FROM my_table;
```
