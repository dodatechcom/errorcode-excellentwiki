---
title: "[Solution] Prometheus Metric Name Invalid"
description: "How to fix invalid metric name errors in Prometheus"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Metric name contains invalid characters (only [a-zA-Z_:])
- Name starts with underscore or colon
- Name exceeds maximum length
- Reserved words used as metric names

## How to Fix

Use valid metric naming conventions:

```python
# Wrong
counter = Counter('my-metric', 'Help')       # hyphen invalid
counter = Counter('123metric', 'Help')        # starts with digit
counter = Counter('my.metric', 'Help')        # dot invalid

# Correct
counter = Counter('my_metric_total', 'Help')  # underscore + _total suffix
counter = Counter('http_requests_total', 'Help')
```

Valid metric name rules:

```bash
# Must match: [a-zA-Z_:][a-zA-Z0-9_:]*
# Convention: namespace_subsystem_name_unit_total/info/created
# Examples:
#   http_requests_total
#   node_cpu_seconds_total
#   go_goroutines
```

Check existing metric names:

```bash
curl -s http://localhost:9090/api/v1/label/__name__/values | jq '.data[]'
```

## Examples

```bash
# Query specific metric
curl -s 'http://localhost:9090/api/v1/query?query=http_requests_total'

# List all metric names
curl -s http://localhost:9090/api/v1/label/__name__/values | jq -r '.data[]' | head -20
```
