---
title: "[Solution] Prometheus Alert Not Firing"
description: "How to fix Prometheus alerts that should fire but do not"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Alert expression evaluating to false
- Metric not available or missing labels
- `for` duration not yet satisfied
- Rule file not loaded or has syntax errors
- Evaluation interval too slow

## How to Fix

Test alert expression manually:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=<alert-expr>'
```

Check if rules are loaded:

```bash
curl -s http://localhost:9090/api/v1/rules | jq '.data.groups[].rules[] | select(.type == "alerting") | .name'
```

Validate rule file:

```bash
promtool check rules alert-rules.yml
```

Verify evaluation interval:

```yaml
groups:
  - name: alerts
    interval: 15s  # Default is global evaluation_interval
    rules:
      - alert: MyAlert
        expr: up == 0
        for: 2m
```

## Examples

```bash
# Check rule evaluation
curl -s http://localhost:9090/api/v1/rules | jq '.data.groups[] | .rules[] | select(.type == "alerting") | {name: .name, state: .state, evaluations: .evaluationFailures}'

# Test expression
curl -s 'http://localhost:9090/api/v1/query?query=up == 0'

# Reload rules
kill -HUP $(pidof prometheus)
```
