---
title: "[Solution] InfluxDB Task Flux Error"
description: "How to fix InfluxDB task Flux script errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Flux syntax error in task
- Flux function not available
- Flux script too complex

## How to Fix

```bash
influx task create --org myorg --name mytask --every 1h --flux 'from(bucket:"mybucket") |> range(start:-1h) |> filter(fn:(r) => r._measurement == "cpu") |> mean() |> to(bucket:"hourly",org:"myorg")'
```

## Examples

```bash
influx task list --org myorg
```
