---
title: "[Solution] ClickHouse Format Function Error"
description: "How to fix ClickHouse FORMAT and output errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- FORMAT not specified
- Output format wrong
- FORMAT not supported for query

## How to Fix

```sql
SELECT * FROM mytable FORMAT JSON;
```

## Examples

```sql
SELECT * FROM mytable FORMAT CSV;
SELECT * FROM mytable FORMAT TabSeparatedWithNames;
```
