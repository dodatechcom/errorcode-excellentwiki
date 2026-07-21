---
title: "[Solution] Prometheus Infinity Value Error"
description: "How to fix Inf (Infinity) values appearing in Prometheus queries"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Division by zero producing positive or negative infinity
- Exponential function overflow
- Binary operations with mismatched series
- Incorrect rate calculation on counter resets

## How to Fix

Clamp infinite values:

```promql
# Clamp to a maximum value
clamp_max(metric_name, 1e9)

# Clamp to zero if infinite
metric_name == metric_name
```

Guard against zero denominators:

```promql
# Wrong: division by zero produces Inf
rate(errors_total[5m]) / rate(total[5m])

# Correct
(rate(errors_total[5m]) > 0) / (rate(total[5m]) > 0)
```

## Examples

```bash
# Find infinite values
curl -s 'http://localhost:9090/api/v1/query?query=metric_name == Inf'

# Safe query with clamping
curl -s 'http://localhost:9090/api/v1/query?query=clamp_max(rate(errors_total[5m]) / rate(total[5m]), 1)'
```
