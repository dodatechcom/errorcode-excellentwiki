---
title: "[Solution] InfluxDB Flux Empty Result Error"
description: "How to fix InfluxDB Flux empty query result errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Time range has no data
- Filter too restrictive
- Wrong bucket name

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -24h)
  |> filter(fn: (r) => r._measurement == "cpu")
```

## Examples

```bash
influx query 'from(bucket: "mybucket") |> range(start: -1h) |> group() |> count()'
```
