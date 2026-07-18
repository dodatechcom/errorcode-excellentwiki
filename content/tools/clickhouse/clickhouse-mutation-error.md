---
title: "[Solution] ClickHouse Mutation Error — How to Fix"
description: "Fix ClickHouse mutation errors including failed mutations, stuck mutations, and mutation-related performance issues"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Mutation Error

Mutations in ClickHouse are ALTER TABLE operations that modify existing data (DELETE, UPDATE). Mutation errors occur when mutations fail, get stuck, or cause performance issues.

## Why It Happens

- The mutation is blocked by a merge in progress
- Disk space runs out during mutation execution
- The mutation query is syntactically incorrect
- The mutation is too large and times out
- A concurrent mutation conflicts with an existing one
- ZooKeeper is unavailable for replicated table mutations

## Common Error Messages

```
Code: 225. DB::Exception: Mutation 0000000001 is not done
```

```
Code: 396. DB::Exception: Mutation is not possible: table is readonly
```

```
Code: 241. DB::Exception: Memory limit exceeded while executing mutation
```

```
Code: 252. DB::Exception: Cannot mutate column because of concurrent mutation
```

## How to Fix It

### 1. Check Mutation Status

```sql
-- See all mutations and their progress
SELECT database, table, mutation_id, command, is_done, parts_to_do
FROM system.mutations
WHERE is_done = 0;

-- Check mutation progress
SELECT * FROM system.mutations WHERE database = 'mydb';
```

### 2. Kill a Stuck Mutation

```sql
-- Kill a specific mutation
KILL MUTATION WHERE database = 'mydb' AND table = 'events' AND mutation_id = '0000000001';

-- Verify it is killed
SELECT * FROM system.mutations WHERE is_done = 0;
```

### 3. Fix Mutation Performance

```sql
-- Reduce mutation impact on reads
ALTER TABLE events DELETE WHERE date < '2024-01-01'
SETTINGS mutations_sync = 0,  -- async (default)
  max_threads_for_mutations = 4;

-- Or run synchronously (waits for completion)
ALTER TABLE events DELETE WHERE date < '2024-01-01'
SETTINGS mutations_sync = 1;
```

### 4. Fix Concurrent Mutation Conflicts

```sql
-- Check if another mutation is running
SELECT * FROM system.mutations WHERE is_done = 0;

-- Wait for existing mutation to complete
-- Then run the new mutation

-- Or kill the existing mutation if it is stuck
KILL MUTATION WHERE database = 'mydb' AND table = 'events';
```

## Common Scenarios

- **DELETE mutation is slow**: The mutation reads all parts. Break into smaller batches by date range.
- **Mutation stuck on readonly table**: The table is readonly due to ZooKeeper issues. Fix ZooKeeper first.
- **Too many pending mutations**: Queue mutations and run them sequentially.

## Prevent It

- Run mutations during low-traffic periods
- Break large mutations into smaller date-range batches
- Monitor `system.mutations` for stuck or failed mutations

## Related Pages

- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse Merge Error](/tools/clickhouse/clickhouse-merge-error)
- [ClickHouse Replication Error](/tools/clickhouse/clickhouse-replication-error)
