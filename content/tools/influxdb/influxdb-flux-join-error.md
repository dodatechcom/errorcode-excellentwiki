---
title: "[Solution] InfluxDB Flux Union Error"
description: "How to fix InfluxDB Flux union function errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Union producing duplicate columns
- Schema mismatch between tables
- Union producing too many rows

## How to Fix

```flux
t1 = from(bucket: "mybucket") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "cpu")
t2 = from(bucket: "mybucket") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "disk")
union(tables: [t1, t2])
```

## Examples

```flux
from(bucket: "mybucket") |> range(start: -1h) |> group() |> distinct(column: "host")
```
