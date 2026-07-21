---
title: "InfluxDB Flux Join Error Code"
description: "Flux join with specific error code"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Flux join function returning specific error code.

## Common Causes
- Table schema mismatch
- Join key not found
- Empty tables

## How to Fix
```flux
a = from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")

b = from(bucket: "mydb")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "mem")
  |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")

join(tables: {a: a, b: b}, on: ["_time", "host"])
```

## Examples
```flux
// Correct join usage
left = from(bucket: "mydb") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "cpu")
right = from(bucket: "mydb") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "mem")
join(tables: {left: left, right: right}, on: ["_time"])
```

