---
title: "[Solution] InfluxDB Cardinality Error — How to Fix"
description: "Fix InfluxDB cardinality errors including high series cardinality, performance degradation, and cardinality management issues"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Cardinality Error

Cardinality errors in InfluxDB occur when the number of unique time series exceeds the system's capacity. High cardinality degrades performance and causes memory issues.

## Why It Happens

- High-cardinality tags (e.g., UUID, request_id) create millions of series
- Tags are added dynamically without control
- The number of unique tag combinations grows unbounded
- The database has too many measurements with high cardinality

## Common Error Messages

```
error: too many series
```

```
partial write: max-series-per-database exceeded
```

```
write failed: database is full due to series limit
```

```
query error: memory allocation exceeded due to cardinality
```

## How to Fix It

### 1. Check Current Cardinality

```influxql
SHOW SERIES CARDINALITY
SHOW DATABASE CARDINALITY
SHOW MEASUREMENT CARDINALITY ON mydb
```

### 2. Reduce Tag Cardinality

```bash
# Move high-cardinality values from tags to fields
# BAD: creates millions of series
# cpu,request_id=abc123 value=50

# GOOD: use fields for high-cardinality values
# cpu,host=server01 request_id="abc123",value=50
```

### 3. Configure Series Limits

```bash
# In influxdb.conf
[data]
  max-series-per-database = 1000000
  max-values-per-tag = 100000
```

### 4. Drop High-Cardinality Data

```influxql
-- Drop specific measurements
DROP MEASUREMENT events

-- Or delete specific series
DELETE FROM cpu WHERE request_id = 'abc123'
```

## Common Scenarios

- **UUID as tag causes millions of series**: Move UUID to a field.
- **Dynamic tags from user input**: Control tag values with a whitelist.
- **Query OOMs due to high cardinality**: Aggregate before returning results.

## Prevent It

- Limit the number of unique tag values per measurement
- Use fields instead of tags for high-cardinality values
- Monitor series cardinality with `SHOW SERIES CARDINALITY`

## Related Pages

- [InfluxDB Query Error](/tools/influxdb/influxdb-query-error)
- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Memory Error](/tools/influxdb/influxdb-oom-error)
