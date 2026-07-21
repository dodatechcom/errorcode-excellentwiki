---
title: "InfluxDB Flux Filter Error Code"
description: "Flux filter with specific error code"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux filter returning specific error code.

## Common Causes
- Filter predicate error
- Column not found
- Type mismatch

## How to Fix
```flux
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu" and r._field == "usage_user")
```

## Examples
```flux
// Correct filter usage
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> filter(fn: (r) => r._value > 0.5)
```

