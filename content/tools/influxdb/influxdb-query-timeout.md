---
title: "InfluxDB Query Timeout"
description: "Query operations timing out"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Queries are timing out before returning results.

## Common Causes
- Large time range queries
- Complex aggregations
- Insufficient resources

## How to Fix
```yaml
[query]
  query-timeout = 30s
  max-select-buckets = 0
```

## Examples
```flux
// Optimize query with smaller time range
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> aggregateWindow(every: 5m, fn: mean)
```

