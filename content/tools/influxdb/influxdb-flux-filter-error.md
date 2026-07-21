---
title: "[Solution] InfluxDB Flux Filter Error"
description: "How to fix InfluxDB Flux filter function errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Filter predicate returning wrong type
- Filter too restrictive
- Regex in filter not matching

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu" and r.host == "server01")
```

## Examples

```flux
from(bucket: "mybucket") |> range(start: -1h) |> filter(fn: (r) => r._value > 50.0)
```
