---
title: "[Solution] ScyllaDB Timeout Error — How to Fix"
description: "Fix ScyllaDB timeout errors by tuning read/write timeouts, increasing driver timeout settings, and optimizing slow queries"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Timeout Error

ScyllaDB timeout errors occur when queries exceed the configured timeout threshold. Timeouts can happen at the client, coordinator, or replica level.

## Why It Happens

- Query is too slow for the configured timeout
- Coordinator cannot reach replica nodes
- Large partition reads exceed timeout
- Compaction or repair is consuming I/O resources
- Client driver timeout is shorter than server timeout
- Too many concurrent requests overwhelm the server

## Common Error Messages

```
ReadTimeout: Server responded too slowly
```

```
WriteTimeout: Operation timed out for table
```

```
RequestTimeout: Client request timeout
```

```
OperationTimedOut: errors={10.0.0.1:9042: 'timed out'}
```

## How to Fix It

### 1. Increase Timeout Settings

```yaml
# In scylla.yaml
read_request_timeout_in_ms: 30000     # 30 seconds
write_request_timeout_in_ms: 30000    # 30 seconds
range_request_timeout_in_ms: 60000    # 60 seconds
```

```python
# Driver timeout settings
from cassandra.cluster import Cluster

cluster = Cluster(
    ['10.0.0.1'],
    connect_timeout=30,
    request_timeout=60
)
```

### 2. Optimize Slow Queries

```bash
# Enable query tracing
cqlsh> TRACING ON;
cqlsh> SELECT * FROM users WHERE id = '1';

# Check query plan
nodetool tablestats mykeyspace.mytable
```

```cql
-- BAD: full table scan
SELECT * FROM users WHERE age > 18 ALLOW FILTERING;

-- GOOD: use indexed column with partition key
CREATE INDEX ON users (age);
SELECT * FROM users WHERE user_id = '1' AND age > 18;
```

### 3. Monitor and Tune Performance

```bash
# Check slow queries
grep -i "slow query" /var/log/scylla/scylla.log | tail -20

# Monitor latency percentiles
nodetool proxyhistograms

# Check pending requests
nodetool tpstats | grep -E "(Read|Write)Stage"
```

```yaml
# Increase native transport threads if overloaded
native_transport_max_threads: 128
native_transport_max_frame_size_in_mb: 16
```

### 4. Split Large Queries

```python
# Paginate large result sets
statement = SimpleStatement(
    "SELECT * FROM users WHERE status = 'active'",
    fetch_size=100
)
for row in session.execute(statement):
    process(row)

# Use token-range queries for large scans
query = "SELECT * FROM users WHERE token(id) > token(?) AND token(id) <= token(?)"
```

## Common Scenarios

- **Dashboard times out on aggregation**: Use materialized views or pre-computed counters.
- **Write timeout during peak load**: Increase `native_transport_max_threads`.
- **Read timeout on large partition**: Split partition or reduce partition size.

## Prevent It

- Set appropriate fetch_size for large result sets
- Monitor `ReadTimeout` and `WriteTimeout` metrics
- Use query tracing to identify slow operations

## Related Pages

- [ScyllaDB Connection Error](/tools/scylladb/scylladb-connection-error)
- [ScyllaDB Query Error](/tools/scylladb/scylladb-query-error)
- [ScyllaDB Consistency Error](/tools/scylladb/scylladb-consistency-error)
