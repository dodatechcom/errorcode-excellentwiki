---
title: "[Solution] InfluxDB Flux Syntax Error"
description: "How to fix InfluxDB Flux syntax errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Flux language syntax error
- Missing import statement
- Incorrect pipe operator usage

## How to Fix

```flux
from(bucket: "mybucket")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
```

## Examples

```bash
influx query 'from(bucket: "mybucket") |> range(start: -1h) |> limit(n: 5)'
```
