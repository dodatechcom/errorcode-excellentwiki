---
title: "[Solution] Prometheus Metric Family Name Error"
description: "How to fix metric family name conflicts in Prometheus exposition format"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Same metric name with different types (counter vs gauge)
- Metric type changed without changing name
- Mixed metric types in the same output
- Exposition format errors causing type mismatch

## How to Fix

Ensure consistent metric types:

```python
# Wrong: changing type of existing metric
REGISTRY.unregister(old_counter)
REGISTRY.register(new_gauge)  # same name, different type

# Correct: use a new name
COUNTER_TOTAL = Counter('requests_total', 'Total requests')
GAUGE_CURRENT = Gauge('requests_current', 'Current requests')
```

Check metric types on a target:

```bash
curl -s http://target:8080/metrics | grep -E "^# TYPE"
```

Restart target after changing metric types:

```bash
sudo systemctl restart my-app
```

## Examples

```bash
# View metric types
curl -s http://localhost:8080/metrics | grep "^# TYPE"

# Check for type conflicts
curl -s http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_series
```
