---
title: "[Solution] Prometheus Recording Rules Error"
description: "Fix Prometheus recording rules errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Recording Rules Error

Prometheus recording rule errors occur when rules fail to evaluate or produce incorrect results.

## Why This Happens

- Rule syntax invalid
- Evaluation error
- High memory usage
- Rule not matching

## Common Error Messages

- `rule_syntax_error`
- `rule_evaluation_error`
- `rule_memory_error`
- `rule_not_matching`

## How to Fix It

### Solution 1: Define recording rules

Create recording rules:

```yaml
group:
  name: my_rules
  rules:
    - record: job:http_requests:rate5m
      expr: rate(http_requests_total[5m])
```

### Solution 2: Optimize rule evaluation

Adjust evaluation interval:

```yaml
group:
  name: my_rules
  interval: 30s
  rules: [...]
```

### Solution 3: Check rule health

View rule status in the Rules page.


## Common Scenarios

- **Rule not evaluating:** Check the PromQL expression.
- **High memory usage:** Optimize the expression or reduce rule scope.

## Prevent It

- Test rules in UI
- Monitor evaluation duration
- Document rule changes
