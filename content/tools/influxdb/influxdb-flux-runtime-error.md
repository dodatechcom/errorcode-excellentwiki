---
title: "InfluxDB Flux Runtime Error"
description: "Flux runtime execution error"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux runtime error during query execution.

## Common Causes
- Script execution timeout
- Memory limit exceeded
- Invalid function call

## How to Fix
```flux
// Optimize query
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> aggregateWindow(every: 5m, fn: mean)
```

## Examples
```flux
// Check Flux runtime settings
option task = {name: "test", every: 1h}
from(bucket: "mydb") |> range(start: -1h) |> mean()
```

