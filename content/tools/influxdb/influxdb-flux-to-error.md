---
title: "[Solution] InfluxDB Flux To Error"
description: "How to fix InfluxDB Flux to function errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Target bucket not found
- Schema mismatch
- Permission denied on target bucket

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -24h)
  |> to(bucket: "downsampled", org: "myorg")
```

## Examples

```flux
from(bucket: "mybucket") |> range(start: -1h) |> aggregateWindow(every: 1h, fn: mean) |> to(bucket: "hourly", org: "myorg")
```
