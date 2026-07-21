---
title: "InfluxDB Flux Array Error"
description: "Flux array operation error"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux array operations are producing errors.

## Common Causes
- Index out of bounds
- Array type mismatch
- Invalid array slice

## How to Fix
```flux
array = [1, 2, 3, 4, 5]

from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
```

## Examples
```flux
// Correct array usage
arr = [1, 2, 3]
result = arrays.sort(arr: arr)
```

