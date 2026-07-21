---
title: "InfluxDB Flux Yield Error"
description: "Flux yield function error"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux yield function producing unexpected results.

## Common Causes
- Multiple yield calls
- Missing yield in subquery
- Yield name conflict

## How to Fix
```flux
// Single yield per query
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> yield(name: "result")
```

## Examples
```flux
// Named yield for multiple results
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> yield(name: "cpu-data")
```

