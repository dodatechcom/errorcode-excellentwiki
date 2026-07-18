---
title: "[Solution] ScyllaDB Range Error — How to Fix"
description: "Fix ScyllaDB range errors by correcting token range queries, resolving range scan timeouts, and fixing token allocation issues"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Range Error

ScyllaDB range errors occur when token range queries fail or return incorrect results. Range queries are used for scanning data across partitions.

## Why It Happens

- Token range query exceeds timeout
- Range boundaries do not match any partition tokens
- Query range is too large for memory
- Partitioner configuration is inconsistent across nodes
- Token allocation is uneven across nodes
- Range scan triggers excessive I/O

## Common Error Messages

```
RangeError: Token range query timed out
```

```
InvalidRequest: Range start and end must be on same partition
```

```
ReadTimeout: Range scan too slow
```

```
InvalidRequest: Invalid token range
```

## How to Fix It

### 1. Use Token Range Queries Correctly

```cql
-- Query using token() function
SELECT * FROM users
WHERE token(id) > token('user_1')
AND token(id) <= token('user_100');

-- Query specific token range
SELECT * FROM events
WHERE token(event_id) > -9223372036854775808
AND token(event_id) < 0;

-- Paginate large range queries
SELECT * FROM users
WHERE token(id) > token('last_seen_id')
LIMIT 1000;
```

### 2. Fix Token Range Timeouts

```python
# Increase timeout for range queries
from cassandra.query import SimpleStatement

statement = SimpleStatement(
    "SELECT * FROM users WHERE token(id) > token(0)",
    fetch_size=1000,
    timeout=120
)
for row in session.execute(statement):
    process(row)
```

### 3. Check Token Distribution

```bash
# View token ring
nodetool ring

# Check for uneven distribution
nodetool ring | awk '{print $1, $NF}' | sort -k2 -n

# Verify partitioner
nodetool describecluster | grep Partitioner
```

### 4. Optimize Range Queries

```cql
-- Use clustering key instead of token range for exact lookups
SELECT * FROM users WHERE user_id = 'user_1';

-- Use smaller ranges with pagination
SELECT * FROM events
WHERE token(event_id) > token('batch_001')
AND token(event_id) <= token('batch_010')
LIMIT 500;

-- Use count() for range statistics instead of fetching all rows
SELECT COUNT(*) FROM users
WHERE token(id) > token(0);
```

## Common Scenarios

- **Range query times out**: Reduce range size or increase fetch_size.
- **Uneven data distribution**: Rebalance tokens using `nodetool movetoken`.
- **Range scan on large table**: Paginate results and use appropriate fetch_size.

## Prevent It

- Use token-range pagination instead of full scans
- Monitor data distribution across the token ring
- Design data model to minimize range query needs

## Related Pages

- [ScyllaDB Query Error](/tools/scylladb/scylladb-query-error)
- [ScyllaDB Partitioner Error](/tools/scylladb/scylladb-partitioner-error)
- [ScyllaDB Timeout Error](/tools/scylladb/scylladb-timeout-error)
