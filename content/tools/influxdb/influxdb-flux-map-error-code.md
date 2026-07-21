---
title: "InfluxDB Flux Map Error Code"
description: "Flux map with specific error code"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux map function returning specific error code.

## Common Causes
- Return record invalid
- Missing required columns
- Type conversion error

## How to Fix
```flux
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> map(fn: (r) => ({r with _value: r._value * 100}))
```

## Examples
```flux
// Correct map usage
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> map(fn: (r) => ({_time: r._time, host: r.host, value: r._value}))
```

