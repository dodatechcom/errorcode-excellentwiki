---
title: "InfluxDB Flux Group Error Code"
description: "Flux group with specific error code"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux group function returning specific error code.

## Common Causes
- Invalid group key
- Column not found
- Empty group

## How to Fix
```flux
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> group(columns: ["host"])
```

## Examples
```flux
// Correct group usage
from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> group()
  |> mean()
```

