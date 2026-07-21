---
title: "[Solution] InfluxDB Notification Endpoint Error"
description: "How to fix InfluxDB notification endpoint errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Endpoint URL unreachable
- Authentication failed
- Endpoint type mismatch

## How to Fix

```bash
influx endpoint create myendpoint --org myorg --type slack --url https://hooks.slack.com/services/XXX
```

## Examples

```bash
influx endpoint list --org myorg
```
