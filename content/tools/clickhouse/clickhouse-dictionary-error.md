---
title: "[Solution] ClickHouse Dictionary Error — How to Fix"
description: "Fix ClickHouse dictionary errors including load failures, refresh issues, and dictionary source connection problems"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Dictionary Error

Dictionary errors in ClickHouse occur when external dictionaries fail to load, refresh, or serve data. Dictionaries provide fast key-value lookups from external sources.

## Why It Happens

- The dictionary source (MySQL, PostgreSQL, HTTP) is unreachable
- The dictionary definition has invalid SQL or configuration
- The dictionary is too large to fit in memory
- The refresh interval causes performance issues
- The dictionary structure does not match the source data
- The ClickHouse server cannot connect to the dictionary source

## Common Error Messages

```
Code: 225. DB::Exception: Failed to load dictionary 'my_dict'
```

```
Code: 210. DB::Exception: Connection refused to dictionary source
```

```
Code: 47. DB::Exception: Unknown column 'xxx' in dictionary definition
```

```
Code: 241. DB::Exception: Memory limit exceeded while loading dictionary
```

## How to Fix It

### 1. Check Dictionary Status

```sql
-- Check if dictionary is loaded
SELECT name, status, loading_duration_ms
FROM system.dictionaries;

-- Check dictionary structure
SELECT name, key, attribute, type
FROM system.dictionary_structure
WHERE database = 'default';
```

### 2. Fix Dictionary Source Connection

```bash
# Test connection to dictionary source (e.g., MySQL)
mysql -h mysql-host -u dict_user -p -e "SELECT 1"

# Check if the source is reachable from ClickHouse
clickhouse-client --query "
SELECT * FROM system.dictionaries
WHERE name = 'my_dict'"
```

### 3. Fix Dictionary Definition

```sql
-- Drop and recreate dictionary
DROP DICTIONARY IF EXISTS my_dict;

CREATE DICTIONARY my_dict (
  id UInt64,
  name String,
  status String
)
PRIMARY KEY id
SOURCE(MYSQL(
  HOST 'mysql-host'
  PORT 3306
  USER 'dict_user'
  PASSWORD 'pass'
  DB 'mydb'
  TABLE 'users'
))
LAYOUT(HASH_TABLE())
LIFETIME(MIN 300 MAX 600)
```

### 4. Fix Memory Issues with Large Dictionaries

```sql
-- Use a more memory-efficient layout
-- BAD: HASH_TABLE for millions of keys
-- GOOD: FLAT for up to 10K keys, HASH_TABLE for up to 10M, CACHE for larger

CREATE DICTIONARY my_dict (
  id UInt64,
  name String
)
PRIMARY KEY id
SOURCE(...)
LAYOUT(CACHE(MAX_SIZE_IN_CELLS 1000000))
```

## Common Scenarios

- **Dictionary fails to load after source restart**: Set `LIFETIME(MIN 60 MAX 300)` for periodic refresh.
- **Dictionary too large for memory**: Use CACHE layout instead of HASH_TABLE.
- **Dictionary source query is slow**: Optimize the source query or add caching.

## Prevent It

- Monitor dictionary load status in `system.dictionaries`
- Use appropriate layout for dictionary size (FLAT, HASH_TABLE, CACHE)
- Set reasonable LIFETIME to refresh dictionaries without overwhelming the source

## Related Pages

- [ClickHouse Connection Error](/tools/clickhouse/clickhouse-connection-error)
- [ClickHouse Query Error](/tools/clickhouse/clickhouse-query-error)
- [ClickHouse Memory Error](/tools/clickhouse/clickhouse-memory-error)
