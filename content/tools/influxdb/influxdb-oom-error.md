---
title: "[Solution] InfluxDB Out of Memory Error — How to Fix"
description: "Fix InfluxDB OOM errors by tuning memory limits, query concurrency, and server configuration for memory-intensive operations"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Out of Memory Error

OOM errors in InfluxDB occur when queries or write operations exceed available memory. This is common with high-cardinality data or complex Flux queries.

## Why It Happens

- A query processes too many series (high cardinality)
- The Flux query allocates too much memory for intermediate results
- Write batches are too large for available memory
- Multiple concurrent queries exhaust memory
- The query-cache is too large
- The server does not have enough RAM for the workload

## Common Error Messages

```
error: memory allocation exceeded
```

```
flux runtime error: exceeded memory allocation
```

```
write failed: server returned HTTP status 503
```

```
Killed process 12345 (influxd)
```

## How to Fix It

### 1. Configure Memory Limits

```bash
# In influxdb.conf
[storage]
  cache-max-memory-size = "1g"
  cache-snapshot-memory-size = "256k"

[coordinator]
  max-concurrent-queries = 10
  query-timeout = "30s"
```

### 2. Reduce Query Memory Usage

```flux
// BAD: returns millions of data points
from(bucket: "mydb")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "events")

// GOOD: aggregate first
from(bucket: "mydb")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "events")
  |> aggregateWindow(every: 1h, fn: mean)
```

### 3. Reduce Cardinality

```influxql
-- Check series count
SHOW SERIES CARDINALITY
SHOW DATABASE CARDINALITY

-- Remove high-cardinality tags from measurements
-- BAD: user_id as a tag creates millions of series
-- GOOD: use user_id as a field instead
```

### 4. Limit Concurrent Queries

```bash
# In influxdb.conf
[coordinator]
  max-concurrent-queries = 5
  query-timeout = "30s"
  log-queries-after = "10s"
```

## Common Scenarios

- **Flux query OOMs on 30-day range**: Aggregate before returning results.
- **High cardinality causes memory pressure**: Remove high-cardinality tags or use fields.
- **Concurrent queries exhaust memory**: Reduce `max-concurrent-queries`.

## Prevent It

- Monitor series cardinality with `SHOW SERIES CARDINALITY`
- Set `query-timeout` to kill long-running queries
- Use `aggregateWindow` in Flux queries to reduce data volume

## Related Pages

- [InfluxDB Query Error](/tools/influxdb/influxdb-query-error)
- [InfluxDB Flux Error](/tools/influxdb/influxdb-flux-error)
- [InfluxDB Cardinality Error](/tools/influxdb/influxdb-cardinality-error)
