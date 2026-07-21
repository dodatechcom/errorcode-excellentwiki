---
title: "[Solution] InfluxDB Flux Group Error"
description: "How to fix InfluxDB Flux group function errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Group producing too many tables
- Group key not matching expected columns
- Ungroup producing memory error

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -1h)
  |> group(columns: ["host"])
  |> mean()
```

## Examples

```flux
from(bucket: "mybucket") |> range(start: -1h) |> group() |> count()
```
