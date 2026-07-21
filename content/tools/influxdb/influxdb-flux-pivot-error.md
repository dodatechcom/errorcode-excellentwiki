---
title: "[Solution] InfluxDB Flux Pivot Error"
description: "How to fix InfluxDB Flux pivot function errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Pivot producing too many columns
- Missing pivot keys
- Value column type mismatch

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -1h)
  |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
```

## Examples

```flux
from(bucket: "mybucket") |> range(start: -1h) |> pivot(rowKey: ["_time", "host"], columnKey: ["_field"], valueColumn: "_value")
```
