---
title: "[Solution] InfluxDB Flux Timezone Error"
description: "How to fix InfluxDB Flux timezone conversion errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Timezone string not recognized
- Timezone offset wrong
- DST transition issues

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -24h)
  |> aggregateWindow(every: 1h, fn: mean)
  |> set(key: "timezone", value: "America/New_York")
```

## Examples

```flux
import "timezone"
timezone.location(name: "America/New_York")
```
