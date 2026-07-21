---
title: "[Solution] InfluxDB Task ID Error"
description: "How to fix InfluxDB task ID errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Task ID not found
- Task ID format wrong
- Task deleted

## How to Fix

```bash
influx task list --org myorg
```

## Examples

```bash
influx task find --org myorg
```
