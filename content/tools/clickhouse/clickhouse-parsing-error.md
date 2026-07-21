---
title: "[Solution] ClickHouse Parsing Error"
description: "How to fix ClickHouse data parsing errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Data type conversion failure
- Incorrect date/time format
- Special characters not escaped
- Numeric overflow during parse

## How to Fix

Check data format:

```sql
SELECT toUInt32OrDefault('abc');  -- returns 0
SELECT toDateOrDefault('bad-date');  -- returns 1970-01-01
```

Use safe parsing functions:

```sql
SELECT toInt32OrZero(value), toString(value) FROM my_table;
```

## Examples

```sql
SELECT toInt32OrDefault('not_a_number');
SELECT parseDateTimeBestEffort('2024/01/01 12:00:00');
```
