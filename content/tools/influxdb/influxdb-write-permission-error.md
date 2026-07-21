---
title: "[Solution] InfluxDB Write Permission Error"
description: "How to fix InfluxDB write permission denied errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Token lacks write permission
- Bucket not accessible
- Organization mismatch

## How to Fix

```bash
influx auth create --org myorg --read-bucket 000 --write-bucket 000
```

## Examples

```bash
influx auth find --org myorg
```
