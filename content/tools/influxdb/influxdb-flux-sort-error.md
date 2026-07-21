---
title: "[Solution] InfluxDB Flux Sort Error"
description: "How to fix InfluxDB Flux sort function errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Sort column not found
- Sorting mixed types
- Descending sort not working

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -1h)
  |> sort(columns: ["_value"], desc: true)
```

## Examples

```flux
from(bucket: "mybucket") |> range(start: -1h) |> sort(columns: ["_time"], desc: true) |> limit(n: 10)
```
