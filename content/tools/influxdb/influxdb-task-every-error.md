---
title: "[Solution] InfluxDB Task Every Error"
description: "How to fix InfluxDB task interval errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Task every interval too short
- Task every interval too long
- Task every interval format wrong

## How to Fix

```bash
influx task create --org myorg --name mytask --every 1h --flux 'from(bucket:"mybucket") |> range(start:-1h)'
```

## Examples

```bash
influx task list --org myorg
```
