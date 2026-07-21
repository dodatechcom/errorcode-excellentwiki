---
title: "[Solution] ClickHouse Syntax Error"
description: "Fix ClickHouse SQL syntax errors when queries contain invalid ClickHouse dialect"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Syntax Error

Syntax errors occur when SQL queries use syntax not supported by ClickHouse dialect.

## Common Causes

- Using MySQL-specific syntax (LIMIT without OFFSET)
- Missing FROM clause in SELECT
- Invalid JOIN syntax
- Using reserved words as identifiers

## How to Fix

Check ClickHouse SQL reference:

```sql
-- ClickHouse allows SELECT without FROM
SELECT 1 + 1 AS result;
```

Use backticks for identifiers:

```sql
SELECT `order` FROM `order-table`;
```

Fix JOIN syntax:

```sql
SELECT a.id, b.name
FROM table_a AS a
INNER JOIN table_b AS b ON a.id = b.a_id;
```

## Examples

```sql
SELECT number FROM system.numbers LIMIT 10;
```
