---
title: "[Solution] InfluxDB Flux Window Error"
description: "How to fix InfluxDB Flux window function errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Window size too small
- Window overlapping incorrectly
- Every vs period mismatch

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -1h)
  |> window(every: 5m)
  |> mean()
```

## Examples

```flux
from(bucket: "mybucket") |> range(start: -1h) |> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
```
