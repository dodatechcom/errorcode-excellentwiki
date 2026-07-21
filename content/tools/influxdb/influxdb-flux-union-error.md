---
title: "InfluxDB Flux Union Error"
description: "Flux union function error"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux union function failing to combine streams.

## Common Causes
- Schema mismatch between streams
- Too many union inputs
- Column type conflicts

## How to Fix
```flux
// Ensure compatible schemas
a = from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")

b = from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "mem")

union(tables: [a, b])
```

## Examples
```flux
// Union with column matching
union(tables: [
  from(bucket: "db1") |> range(start: -1h),
  from(bucket: "db2") |> range(start: -1h)
])
```

