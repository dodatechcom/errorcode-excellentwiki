---
title: "[Solution] InfluxDB Flux Type Error"
description: "How to fix InfluxDB Flux type mismatch errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Type mismatch in filter
- Incompatible types in math operation
- Wrong function signature

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -1h)
  |> filter(fn: (r) => r._value > 0.0)
```

## Examples

```flux
from(bucket: "mybucket") |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
```
