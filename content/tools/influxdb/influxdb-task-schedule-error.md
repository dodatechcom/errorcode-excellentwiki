---
title: "[Solution] InfluxDB Task Schedule Error"
description: "How to fix InfluxDB task scheduling errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Task not scheduled
- Task schedule overlapping
- Cron expression wrong

## How to Fix

```bash
influx task create --org myorg --name mytask --cron '0 */6 * * *' --flux 'from(bucket:"mybucket") |> range(start:-6h) |> aggregateWindow(every:6h, fn:mean) |> to(bucket:"downsampled",org:"myorg")'
```

## Examples

```bash
influx task list --org myorg | grep -E 'name|cron'
```
