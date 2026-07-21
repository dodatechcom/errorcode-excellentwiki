---
title: "[Solution] InfluxDB Task Log Error"
description: "How to fix InfluxDB task log errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Task log not available
- Task log retention too short
- Task log query syntax wrong

## How to Fix

```bash
influx task log list --org myorg
```

## Examples

```bash
influx task log find --task-id TASK_ID --org myorg
```
