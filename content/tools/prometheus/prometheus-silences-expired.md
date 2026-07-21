---
title: "[Solution] Prometheus Alertmanager Silences Expired"
description: "How to handle expired silences in Alertmanager"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Silence duration too short
- Silence not renewed before expiration
- Default duration not sufficient
- Silences created with past end time

## How to Fix

Check active silences:

```bash
amtool --alertmanager.url=http://localhost:9093 silence query
```

Create longer silences:

```bash
amtool --alertmanager.url=http://localhost:9093 silence add   alertname=HighErrorRate   --duration=24h   --comment="Maintenance window"
```

List and manage silences:

```bash
amtool --alertmanager.url=http://localhost:9093 silence query --active
```

## Examples

```bash
# Query active silences
amtool silence query --alertmanager.url=http://localhost:9093

# Expire a specific silence
amtool silence expire <silence-id> --alertmanager.url=http://localhost:9093

# Create silence via API
curl -X POST http://localhost:9093/api/v2/silences -d '{"matchers":[{"name":"alertname","value":"HighErrorRate"}],"startsAt":"2024-01-01T00:00:00Z","endsAt":"2024-01-02T00:00:00Z"}'
```
