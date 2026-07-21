---
title: "[Solution] Prometheus Alerting Rule Error"
description: "How to fix Prometheus alerting rule configuration errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid PromQL expression in alert rule
- Missing `alert` or `expr` field
- `for` duration too short causing flapping
- Alert annotation templates with errors

## How to Fix

Define proper alerting rules:

```yaml
groups:
  - name: alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

Validate alert rules:

```bash
promtool check rules alert-rules.yml
```

## Examples

```bash
# Validate alert rules
promtool check rules /etc/prometheus/alerts/*.yml

# Test alert expression
curl -s 'http://localhost:9090/api/v1/query?query=rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.1'

# List active alerts
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[] | .labels.alertname'
```
