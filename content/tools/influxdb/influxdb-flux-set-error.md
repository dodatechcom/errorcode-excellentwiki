---
title: "[Solution] InfluxDB Flux Set Error"
description: "How to fix InfluxDB Flux set and keep errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Column not found in set
- Set producing unexpected results
- Keep removing needed columns

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -1h)
  |> set(key: "datacenter", value: "us-east-1")
```

## Examples

```flux
from(bucket: "mybucket") |> range(start: -1h) |> keep(columns: ["_time", "_value", "host"])
```
