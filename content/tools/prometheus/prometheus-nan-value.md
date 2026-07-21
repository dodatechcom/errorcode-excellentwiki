---
title: "[Solution] Prometheus NaN Value Error"
description: "How to fix NaN (Not a Number) values appearing in Prometheus metrics"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Division by zero in PromQL expressions
- Invalid arithmetic operations
- Missing data points in binary operations
- Logarithm of zero or negative numbers
- Histogram quantile with insufficient data

## How to Fix

Guard against division by zero:

```promql
# Wrong: may produce NaN
rate(errors_total[5m]) / rate(requests_total[5m])

# Correct: use > 0 filter
rate(errors_total[5m]) / (rate(requests_total[5m]) > 0)
```

Handle NaN in queries:

```promql
# Replace NaN with 0
clamp_min(metric_name, 0)

# Filter out NaN
metric_name == metric_name
```

Use `default` to handle missing data:

```promql
metric_a / on() group_left() metric_b or vector(0)
```

## Examples

```bash
# Find metrics with NaN
curl -s 'http://localhost:9090/api/v1/query?query=NaN'

# Safe division
curl -s 'http://localhost:9090/api/v1/query?query=rate(errors_total[5m]) / on() group_left() (rate(requests_total[5m]) > 0)'

# Replace NaN with zero
curl -s 'http://localhost:9090/api/v1/query?query=clamp_min(rate(errors_total[5m]) / rate(requests_total[5m]), 0)'
```
