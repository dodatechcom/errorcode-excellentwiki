---
title: "[Solution] Prometheus Alert Fired But Not Resolved"
description: "How to fix Prometheus alerts that fire but do not resolve"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Condition still true when alert should resolve
- `for` duration too short, alert resolves before action taken
- Metric data gap causing repeated firing
- Alertmanager not receiving resolve notification

## How to Fix

Verify alert condition:

```bash
curl -s 'http://localhost:9090/api/v1/alerts' | jq '.data.alerts[] | select(.labels.alertname == "HighErrorRate")'
```

Check alert state transitions:

```bash
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[] | {name: .labels.alertname, state: .state, activeAt: .activeAt}'
```

Increase `for` duration for stability:

```yaml
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
  for: 10m  # Wait longer before firing
```

## Examples

```bash
# View all alerts
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[]'

# Check alert history
curl -s 'http://localhost:9090/api/v1/alerts?state=unresolved'

# Test resolve condition
curl -s 'http://localhost:9090/api/v1/query?query=rate(http_requests_total{status=~"5.."}[5m]) <= 0.1'
```
