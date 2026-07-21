---
title: "[Solution] InfluxDB Notification Rule Error"
description: "How to fix InfluxDB notification rule errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Notification endpoint unreachable
- Rule query syntax wrong
- Status template invalid

## How to Fix

```bash
influx notification rule create myrule --org myorg --endpoint-id ENDPOINT_ID --every 5m --query 'from(bucket:"mybucket") |> range(start:-5m) |> filter(fn:(r) => r._value < 0)'
```

## Examples

```bash
influx notification rule list --org myorg
```
