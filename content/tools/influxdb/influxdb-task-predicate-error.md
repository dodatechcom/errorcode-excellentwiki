---
title: "[Solution] InfluxDB Task Predicate Error"
description: "How to fix InfluxDB task predicate errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Predicate syntax wrong
- Predicate not matching any data
- Predicate too complex

## How to Fix

```bash
influx task create --org myorg --name mytask --every 1h --flux 'from(bucket:"mybucket") |> range(start:-1h) |> filter(fn:(r) => r.host == "server01")'
```

## Examples

```bash
influx task list --org myorg
```
