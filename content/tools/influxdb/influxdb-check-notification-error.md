---
title: "[Solution] InfluxDB Check Notification Error"
description: "How to fix InfluxDB check notification errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Check not linked to notification rule
- Check status not transitioning
- Notification rate limited

## How to Fix

```bash
influx check update mycheck --org myorg --every 5m
```

## Examples

```bash
influx check list --org myorg
```
