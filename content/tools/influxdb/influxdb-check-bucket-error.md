---
title: "[Solution] InfluxDB Check Bucket Error"
description: "How to fix InfluxDB check bucket configuration errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Check bucket not specified
- Check bucket does not exist
- Check bucket retention too short

## How to Fix

```bash
influx check create mycheck --org myorg --query 'from(bucket:"mybucket") |> range(start:-5m) |> filter(fn:(r) => r._value < 0)' --every 5m
```

## Examples

```bash
influx check list --org myorg
```
