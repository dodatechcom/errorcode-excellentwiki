---
title: "[Solution] InfluxDB Bucket Permission Error"
description: "How to fix InfluxDB bucket permission errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Bucket not found
- Permission not granted for bucket
- All-access token required

## How to Fix

```bash
influx auth create --org myorg --read-bucket BUCKET_ID --write-bucket BUCKET_ID
```

## Examples

```bash
influx bucket list --org myorg
```
