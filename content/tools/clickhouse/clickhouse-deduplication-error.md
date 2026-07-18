---
title: "[Solution] ClickHouse Deduplication Error — How to Fix"
description: "Fix ClickHouse deduplication errors including ReplacingMergeTree conflicts, duplicate data handling, and version column issues"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Deduplication Error

Deduplication errors in ClickHouse occur when using ReplacingMergeTree or other deduplication mechanisms. ClickHouse handles deduplication differently from other databases.

## Why It Happens

- The ReplacingMergeTree version column is not set correctly
- Deduplication has not run yet (background merge)
- The ORDER BY key does not uniquely identify rows
- The version column value is the same for duplicates
- Data is inserted multiple times before deduplication runs

## Common Error Messages

```
Code: 252. DB::Exception: Duplicate primary key in ReplacingMergeTree
```

```
Code: 23. DB::Exception: Unexpected duplicate in ReplacingMergeTree
```

```
Code: 131. DB::Exception: Duplicate name found in column list
```

```
Code: 252. DB::Exception: Part already exists
```

## How to Fix It

### 1. Use ReplacingMergeTree Correctly

```sql
-- Define table with version column
CREATE TABLE events (
  id UInt64,
  name String,
  version UInt64,
  event_time DateTime
) ENGINE = ReplacingMergeTree(version)
ORDER BY id;

-- Insert with increasing version
INSERT INTO events VALUES (1, 'event1', 1, now());
INSERT INTO events VALUES (1, 'event1', 2, now());  -- version 2 replaces version 1

-- Deduplication happens during merge
OPTIMIZE TABLE events FINAL;  -- force merge
```

### 2. Force Deduplication

```sql
-- Force merge for deduplication
OPTIMIZE TABLE events FINAL;

-- Check if duplicates still exist
SELECT id, count() FROM events GROUP BY id HAVING count() > 1;
```

### 3. Use argMax for Query-Time Dedup

```sql
-- Query the latest version of each row
SELECT id, argMax(name, version) AS name, max(version) AS version
FROM events
GROUP BY id;
```

### 4. Prevent Duplicates at Insert Time

```sql
-- Use INSERT ... SELECT with deduplication
INSERT INTO events
SELECT id, name, version, event_time
FROM staging_events
WHERE id NOT IN (SELECT id FROM events);

-- Or use ReplacingMergeTree with proper ORDER BY
CREATE TABLE events (
  id UInt64,
  name String,
  version UInt64
) ENGINE = ReplacingMergeTree(version)
ORDER BY (id);  -- deduplication key
```

## Common Scenarios

- **Duplicate rows after insert**: Deduplication has not merged yet. Use `OPTIMIZE TABLE` or `argMax` queries.
- **Wrong version column**: Version column does not increase. Fix insert logic to increment version.
- **ORDER BY does not match dedup key**: ORDER BY must include all dedup key columns.

## Prevent It

- Always use a version column that increases with each update for ReplacingMergeTree
- Use `argMax` in queries to get the latest version regardless of merge state
- Monitor `system.parts` for duplicate parts that indicate merge issues

## Related Pages

- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse Merge Error](/tools/clickhouse/clickhouse-merge-error)
- [ClickHouse Mutation Error](/tools/clickhouse/clickhouse-mutation-error)
