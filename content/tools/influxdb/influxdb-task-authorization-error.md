---
title: "[Solution] InfluxDB Task Authorization Error"
description: "How to fix InfluxDB task authorization errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Task token expired
- Task token lacks permissions
- Task running with wrong org

## How to Fix

```bash
influx auth create --org myorg --read-bucket 000 --write-bucket 000 --read-tasks --write-tasks
```

## Examples

```bash
influx auth find --org myorg
```
