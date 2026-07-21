---
title: "[Solution] Prometheus Recording Rule Conflict Error"
description: "How to fix conflicts between recording rules in Prometheus"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Two recording rules writing to same metric name
- Recording rule output collides with scraped metric
- Circular dependency between recording rules
- Rule group order causing evaluation issues

## How to Fix

Use unique recording rule names:

```yaml
groups:
  - name: app_rules
    rules:
      - record: app:http_requests:rate5m
        expr: sum(rate(http_requests_total[5m])) by (job)
  - name: node_rules
    rules:
      - record: node:cpu:utilization
        expr: 1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))
```

Avoid recording rule names matching scraped metrics:

```bash
# Check if name conflicts with existing metric
curl -s 'http://localhost:9090/api/v1/label/__name__/values' | jq '.data[]' | grep "your_record_name"
```

## Examples

```bash
# List all recording rules
curl -s http://localhost:9090/api/v1/rules | jq '.data.groups[].rules[] | select(.type == "recording") | .name'

# Check for name conflicts
curl -s 'http://localhost:9090/api/v1/query?query=app:http_requests:rate5m'
```
