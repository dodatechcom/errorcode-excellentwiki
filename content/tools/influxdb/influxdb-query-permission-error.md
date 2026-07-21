---
title: "[Solution] InfluxDB Query Permission Error"
description: "How to fix InfluxDB query permission denied errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Token lacks read permission
- Bucket not accessible
- Organization mismatch

## How to Fix

```bash
influx auth create --org myorg --read-bucket 000
```

## Examples

```bash
curl -s -H 'Authorization: Token YOUR_TOKEN' http://localhost:8086/api/v2/query?org=myorg
```
