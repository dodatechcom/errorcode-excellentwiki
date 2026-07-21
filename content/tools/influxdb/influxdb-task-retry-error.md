---
title: "[Solution] InfluxDB Task Retry Error"
description: "How to fix InfluxDB task retry errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Task retry count exceeded
- Retry interval too short
- Task permanently failed

## How to Fix

```bash
influx task retry --task-id TASK_ID --org myorg
```

## Examples

```bash
influx task run list --task-id TASK_ID --org myorg
```
