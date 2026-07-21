---
title: "[Solution] ClickHouse Format Error"
description: "Fix ClickHouse format errors when parsing or outputting data in specific formats"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Format Error

Format errors occur when ClickHouse cannot parse or produce data in the specified format.

## Common Causes

- Input format mismatch with data structure
- Missing required fields in format
- Character encoding issues in CSV/TSV
- JSON format parse error

## How to Fix

Check supported formats:

```sql
SELECT * FROM system.formats;
```

Test format parsing:

```sql
SELECT * FROM format(JSONEachRow, '{"id": 1, "name": "test"}');
```

Use correct format for import:

```bash
clickhouse-client --query="INSERT INTO my_table FORMAT JSONEachRow" < data.json
```

## Examples

```sql
SELECT * FROM my_table FORMAT CSVWithNames;
```
