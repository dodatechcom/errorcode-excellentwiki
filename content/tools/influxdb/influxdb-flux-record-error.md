---
title: "InfluxDB Flux Record Error"
description: "Flux record operation error"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux record operations are producing errors.

## Common Causes
- Missing field
- Invalid record access
- Record type mismatch

## How to Fix
```flux
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> keep(columns: ["_time", "_value", "_field"])
```

## Examples
```flux
// Safe record access
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu" and exists r.host)
```

