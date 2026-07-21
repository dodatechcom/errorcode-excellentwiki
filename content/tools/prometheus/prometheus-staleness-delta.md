---
title: "[Solution] Prometheus Staleness Delta Error"
description: "How to fix Prometheus staleness delta configuration issues"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Staleness delta too short causing false staleness markers
- Staleness delta too long delaying stale series cleanup
- Targets disappearing and reappearing within delta window
- Clock skew affecting staleness detection

## How to Fix

Configure staleness delta:

```yaml
storage:
  tsdb:
    staleness_delta: 5m
```

Default is 5 minutes. Increase for unreliable networks:

```yaml
storage:
  tsdb:
    staleness_delta: 10m
```

Check current staleness settings:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data'
```

## Examples

```bash
# Check for stale markers
curl -s 'http://localhost:9090/api/v1/query?query=stale_nan' | jq '.data.result | length'

# Monitor target uptime
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, lastScrape: .lastScrape}'
```
