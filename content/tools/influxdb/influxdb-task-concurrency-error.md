---
title: "[Solution] InfluxDB Task Concurrency Error"
description: "How to fix InfluxDB task concurrency errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Too many tasks running concurrently
- Task queue full
- Task concurrency limit reached

## How to Fix

```bash
influx task list --org myorg | wc -l
```

## Examples

```bash
influx task list --org myorg | grep -i 'running\|scheduled'
```
