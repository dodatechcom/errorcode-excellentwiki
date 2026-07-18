---
title: "[Solution] ClickHouse Function Not Found Error — How to Fix"
description: "Fix ClickHouse function not found errors by discovering available functions, using correct names, and checking version compatibility"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Function Not Found Error

Function not found errors in ClickHouse occur when using functions that do not exist in the current version or using incorrect function names. ClickHouse has a different function library than MySQL or PostgreSQL.

## Why It Happens

- The function name is misspelled
- The function was added in a newer ClickHouse version
- The function is from a different SQL dialect (MySQL, PostgreSQL)
- The function requires a specific engine or plugin
- The function is deprecated and removed in the current version
- The function requires certain data type arguments

## Common Error Messages

```
Code: 46. DB::Exception: Unknown function 'IFNULL'
```

```
Code: 46. DB::Exception: Unknown function 'GROUP_CONCAT'
```

```
Code: 46. DB::Exception: Unknown function 'DATE_FORMAT'
```

```
Code: 43. DB::Exception: Incorrect number of arguments for function 'concat': expected at least 2, got 1
```

## How to Fix It

### 1. Search for Available Functions

```sql
-- List all functions
SELECT name FROM system.functions ORDER BY name;

-- Search by pattern
SELECT name, syntax, is_aggregate
FROM system.functions
WHERE name LIKE '%string%';

-- Get function details
SELECT * FROM system.functions WHERE name = 'concat';
```

### 2. Use ClickHouse Function Equivalents

```sql
-- MySQL IFNULL -> ifNull
SELECT ifNull(col, 'default');

-- MySQL GROUP_CONCAT -> groupConcat (or arrayStringConcat + groupArray)
SELECT arrayStringConcat(groupArray(name), ', ') FROM t;

-- MySQL DATE_FORMAT -> formatDateTime
SELECT formatDateTime(event_time, '%Y-%m-%d %H:%i:%s') FROM events;

-- MySQL UNIX_TIMESTAMP -> toUnixTimestamp
SELECT toUnixTimestamp(now());
```

### 3. Check ClickHouse Version Compatibility

```sql
SELECT version();

-- Check when a function was introduced
SELECT name, created_in_version
FROM system.functions
WHERE name = 'dateDiff';
```

### 4. Install Required Plugins

```bash
# Some functions require plugins
# Check if a function requires a specific engine
clickhouse-client --query "SELECT * FROM system.functions WHERE name LIKE '%kafka%'"
```

## Common Scenarios

- **Migrating from MySQL**: Use ClickHouse function equivalents. Check `system.functions`.
- **Function not found after upgrade**: Some functions may be renamed. Check release notes.
- **Incorrect number of arguments**: Check the function signature in documentation.

## Prevent It

- Consult ClickHouse function documentation before writing queries
- Use `system.functions` to discover available functions
- Test all functions on the target ClickHouse version before deploying

## Related Pages

- [ClickHouse Function Error](/tools/clickhouse/clickhouse-function-error)
- [ClickHouse Query Error](/tools/clickhouse/clickhouse-query-error)
- [ClickHouse Grammar Error](/tools/clickhouse/clickhouse-grammar-error)
