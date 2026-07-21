---
title: "[Solution] InfluxDB Task Offset Error"
description: "How to fix InfluxDB task offset errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Task offset configuration wrong
- Task running at wrong time
- Task offset too large

## How to Fix

```bash
influx task create --org myorg --name mytask --every 1h --offset 30m --flux 'from(bucket:"mybucket") |> range(start:-1h)'
```

## Examples

```bash
influx task list --org myorg
```
