---
title: "[Solution] InfluxDB Flux Map Error"
description: "How to fix InfluxDB Flux map function errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Map function returning wrong type
- Map function too slow
- Map producing null values

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -1h)
  |> map(fn: (r) => ({r with _value: r._value * 100}))
```

## Examples

```flux
from(bucket: "mybucket") |> range(start: -1h) |> map(fn: (r) => ({_time: r._time, host: r.host, value: r._value}))
```
