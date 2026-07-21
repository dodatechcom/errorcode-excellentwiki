---
title: "InfluxDB Notification Endpoint Error"
description: "Notification endpoint connection failure"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
InfluxDB cannot send notifications to the configured endpoint.

## Common Causes
- Endpoint URL is unreachable
- Authentication credentials expired
- SSL/TLS certificate issues

## How to Fix
```flux
// Test notification endpoint
notification.check(
  check: {name: "test"},
  data: {severity: "crit", message: "test"}
)
```

## Examples
```flux
// List notification endpoints
endpoint.list()
// Update endpoint
endpoint.update(id: "<id>", data: {url: "https://new-webhook.example.com"})
```

