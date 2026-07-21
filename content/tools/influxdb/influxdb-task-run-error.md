---
title: "[Solution] InfluxDB Task Run Error"
description: "How to fix InfluxDB task run errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Task run failing
- Task run timeout
- Task run error in logs

## How to Fix

```bash
influx task run list --task-id TASK_ID --org myorg
```

## Examples

```bash
influx task run logs --task-id TASK_ID --org myorg
```
