---
title: "[Solution] Prometheus Recording Rule Evaluation Error"
description: "Fix Prometheus recording rule evaluation errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Recording Rule Evaluation Error

Prometheus recording rule errors occur when rules fail to evaluate or produce incorrect results.

## Why This Happens

- Expression syntax error
- Evaluation interval too short
- Rule group timeout
- High memory usage

## Common Error Messages

- `recording_rule_syntax_error`
- `recording_rule_interval_error`
- `recording_rule_timeout`
- `recording_rule_memory_error`

## How to Fix It

### Solution 1: Check rule expression

Validate the PromQL expression:

```yaml
group:
  name: my_rules
  rules:
    - record: job:http_requests:rate5m
      expr: rate(http_requests_total[5m])
```

### Solution 2: Adjust evaluation interval

Set appropriate interval:

```yaml
group:
  name: my_rules
  interval: 30s
```

### Solution 3: Monitor rule performance

Check rule evaluation duration.


## Common Scenarios

- **Rule not evaluating:** Verify the PromQL expression is valid.
- **High memory usage:** Optimize the expression or reduce rule scope.

## Prevent It

- Test rules in UI
- Monitor evaluation duration
- Document rule changes
