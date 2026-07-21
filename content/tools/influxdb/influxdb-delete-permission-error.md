---
title: "[Solution] InfluxDB Delete Permission Error"
description: "How to fix InfluxDB delete permission denied errors"
tools: ["influxdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Token lacks delete permission
- Delete API not enabled
- Time range too broad

## How to Fix

```bash
curl -X POST http://localhost:8086/api/v2/delete?org=myorg&bucket=mybucket \
  -H 'Authorization: Token YOUR_TOKEN' \
  -d '{"start":"2024-01-01T00:00:00Z","stop":"2024-01-02T00:00:00Z"}'
```

## Examples

```bash
curl -s -o /dev/null -w '%{http_code}' -X POST http://localhost:8086/api/v2/delete?org=myorg&bucket=mybucket \
  -H 'Authorization: Token YOUR_TOKEN' -d '{"start":"2024-01-01T00:00:00Z","stop":"2024-01-02T00:00:00Z"}'
```
