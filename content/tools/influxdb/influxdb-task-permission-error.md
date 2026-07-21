---
title: "[Solution] InfluxDB Task Permission Error"
description: "How to fix InfluxDB task permission denied errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Task token lacks permissions
- Task not owned by user
- Write permission for target bucket missing

## How to Fix

```bash
influx auth create --org myorg --read-bucket 000 --write-bucket 000 --read-tasks
```

## Examples

```bash
influx task list --org myorg
```
