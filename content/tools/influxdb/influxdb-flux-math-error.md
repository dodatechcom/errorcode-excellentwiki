---
title: "InfluxDB Flux Math Error"
description: "Flux math operation error"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux math operations are producing errors.

## Common Causes
- Division by zero
- Overflow
- Invalid operation

## How to Fix
```flux
import "math"

from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> map(fn: (r) => ({r with _value: math.floor(x: r._value)}))
```

## Examples
```flux
// Safe division
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> map(fn: (r) => ({r with _value: if r._value != 0 then 1.0 / r._value else 0.0}))
```

