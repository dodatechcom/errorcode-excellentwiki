---
title: "[Solution] ClickHouse Dictionary Error"
description: "Fix ClickHouse dictionary errors when external dictionary lookups fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Dictionary Error

Dictionary errors occur when ClickHouse external dictionaries cannot load or query data.

## Common Causes

- Dictionary source unreachable
- Dictionary layout incompatible with query
- Dictionary expired and not refreshed
- Memory limit exceeded for dictionary

## How to Fix

Check dictionary status:

```sql
SELECT name, status, origin, last_exception FROM system.dictionaries;
```

Reload dictionary:

```sql
SYSTEM RELOAD DICTIONARY my_dict;
```

Check dictionary structure:

```sql
SELECT key, attribute FROM my_dict LIMIT 10;
```

## Examples

```sql
SELECT dictGet('my_dict', 'value', key_column) FROM my_table;
```
