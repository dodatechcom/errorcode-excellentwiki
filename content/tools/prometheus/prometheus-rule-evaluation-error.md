---
title: "[Solution] Prometheus Rule Evaluation Error"
description: "How to fix Prometheus rule evaluation errors in recording and alerting rules"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid PromQL expression in rule file
- Circular dependency between recording rules
- Rule referencing non-existent metric
- Rule file syntax error

## How to Fix

Validate rule files:

```bash
promtool check rules rules.yml
```

Correct rule syntax:

```yaml
groups:
  - name: example
    rules:
      - record: job:http_requests:rate5m
        expr: sum(rate(http_requests_total[5m])) by (job)
```

Check for circular dependencies:

```bash
promtool check rules rules.yml 2>&1 | grep "circular"
```

Verify referenced metrics exist:

```bash
curl -s 'http://localhost:9090/api/v1/label/__name__/values' | jq '.data[]' | grep http_requests
```

## Examples

```bash
# Validate all rule files
promtool check rules /etc/prometheus/rules/*.yml

# Check rule evaluation errors
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_rule_evaluation_failures_total'

# List recording rules
curl -s 'http://localhost:9090/api/v1/rules' | jq '.data.groups[] | .rules[] | select(.type == "recording")'
```
