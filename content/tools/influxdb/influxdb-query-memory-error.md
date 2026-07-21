---
title: "[Solution] InfluxDB Query Memory Error — How to Fix"
description: "Fix InfluxDB query memory errors when Flux or InfluxQL queries consume more memory than the configured limit"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Query Memory Error

Query memory errors occur when a Flux or InfluxQL query exceeds the memory limit configured for query execution, causing the query to be killed.

## Why It Happens

- Query scans an unbounded time range without limits
- Large group-by operations consume excessive memory
- Multiple concurrent queries share limited memory pool
- Query uses sort or unique operations on large datasets
- Default memory limit is too low for the workload

## Common Error Messages

```
error: query killed: memory limit exceeded
```

```
runtime error: out of memory during query execution
```

```
error: query exceeded memory allocation: 2147483648 bytes
```

## How to Fix It

### 1. Increase Query Memory Limit

```bash
[coordinator]
  query-memory-limit = 4294967296
  query-max-memory = 8589934592
```

### 2. Add Limits to Queries

```flux
from(bucket: "mydb")
  |> range(start: -24h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> limit(n: 10000)
  |> aggregateWindow(every: 5m, fn: mean)
```

### 3. Use Chunked Results

```bash
curl -XPOST 'http://localhost:8086/api/v2/query?org=myorg' \
  -H 'Authorization: Token mytoken' \
  -H 'Content-Type: application/vnd.flux' \
  -H 'Accept: application/csv' \
  -d 'from(bucket:"mydb") |> range(start:-1h) |> chunked(rows:1000)'
```

### 4. Optimize Group Operations

```flux
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._field == "value")
  |> aggregateWindow(every: 10m, fn: mean, createEmpty: false)
```

## Examples

```
error: query killed: memory limit exceeded (allocated: 2147483648, limit: 2147483648)
```

## Prevent It

- Always add time bounds and limits to queries
- Use aggregateWindow to reduce data volume
- Set query-memory-limit based on available RAM

## Related Pages

- [InfluxDB Query Timeout](/tools/influxdb/influxdb-query-timeout)
- [InfluxDB Memory Error](/tools/influxdb/influxdb-memory-error)
- [InfluxDB OOM Error](/tools/influxdb/influxdb-oom-error)
