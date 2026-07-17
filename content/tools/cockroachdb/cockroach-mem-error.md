---
title: "[Solution] CockroachDB Out of Memory - Fix OOM and Memory Errors"
description: "Fix CockroachDB out of memory errors by tuning cache settings, setting the SQL memory budget, reducing query complexity, and limiting concurrent heavy operation"
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A CockroachDB out of memory error occurs when a node or query consumes more memory than is available. The error message is `out of memory` or `memory budget exceeded` and may cause the node to crash or the query to be cancelled.

## What This Error Means

CockroachDB allocates memory for several components: the SQL memory budget (for sorting, hashing, and aggregations), the cache (for block and row data), and the Go runtime heap. When any of these exceed their limits, the server either cancels the offending query or, in severe cases, the node process is killed by the OS OOM killer.

The error may appear as `SQL memory budget exceeded`, `root: memory budget exceeded`, or `runtime: out of memory` depending on which component exhausted its allocation.

## Why It Happens

- Large sort or hash operations on unbounded result sets
- Query with too many JOINs or GROUP BY on high-cardinality columns
- Memory budget too low for the workload
- Cache size too large relative to available RAM
- Multiple concurrent queries each consuming significant memory
- Node sharing memory with other processes on the same machine
- Go garbage collector not keeping up with allocation rate

## How to Fix It

### 1. Set SQL Memory Limit

```bash
# Start with a specific memory limit
cockroach start \
  --store=path=/var/lib/cockroach/data \
  --max-sql-memory=4GB \
  --cache=2GB \
  --host=0.0.0.0
```

### 2. Tune Memory Settings via SQL

```sql
-- Set the default memory limit for all sessions
ALTER RANGE DEFAULT CONFIGURE ZONE USING gc.ttlseconds = 90000;

-- Set session-level memory limit
SET CLUSTER SETTING sql.defaults.memory_limit = '4GB';
```

### 3. Limit Query Memory Usage

```sql
-- Set a per-query memory limit
SET memory_limit = '512MB';

-- Paginate large queries
SELECT * FROM large_table ORDER BY id LIMIT 1000;
```

### 4. Optimize Memory-Intensive Queries

```sql
-- Instead of sorting the entire table
SELECT * FROM large_table ORDER BY created_at DESC LIMIT 100;

-- Use indexes to avoid in-memory sorts
CREATE INDEX idx_created ON large_table (created_at DESC);
```

### 5. Monitor Memory Usage

```sql
-- Check node memory usage
SELECT * FROM crdb_internal.node_mem_metrics;

-- Check active queries
SHOW QUERIES;
SHOW TRACE FOR SELECT * FROM large_table;
```

### 6. Scale Up Node Memory

```bash
# Increase container or VM memory limit
# CockroachDB recommends at least 8GB RAM per node for production
```

### 7. Reduce Concurrent Memory-Heavy Operations

```yaml
# Limit concurrent connections
SET CLUSTER SETTING server.max_connections = 200;
```

## Common Mistakes

- Setting `--cache` and `--max-sql-memory` to nearly 100% of total RAM, leaving nothing for the OS
- Running CockroachDB alongside other memory-intensive services on the same machine
- Not monitoring `crdb_internal.node_mem_metrics` for memory growth trends
- Using unbounded `SELECT *` queries in application code without `LIMIT`

## Related Pages

- [CockroachDB Timeout](/tools/cockroachdb/cockroach-timeout)
- [CockroachDB Deadlock](/tools/cockroachdb/cockroach-deadlock)
- [CockroachDB Node Unavailable](/tools/cockroachdb/cockroach-node-unavailable)
