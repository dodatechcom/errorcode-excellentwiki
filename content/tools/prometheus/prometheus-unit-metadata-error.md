---
title: "[Solution] Prometheus UNIT Metadata Error"
description: "How to fix UNIT metadata errors in Prometheus exposition format"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Unit suffix does not match metric name convention
- Invalid unit specified in metadata
- Unit not following Prometheus naming convention
- Deprecated unit format

## How to Fix

Follow Prometheus unit conventions:

```python
# Wrong: unit in wrong position or format
GAUGE = Gauge('my_gauge_seconds', 'Help', unit='sec')

# Correct: standard unit suffix
GAUGE = Gauge('my_gauge_seconds', 'Help')
```

Standard unit suffixes:

```bash
# _seconds, _milliseconds, _bytes, _bits, _total
# Examples:
#   http_request_duration_seconds
#   node_memory_total_bytes
#   go_gc_duration_seconds
```

## Examples

```bash
# View unit metadata
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_samples_appended_total'

# Check metric naming
curl -s http://target:8080/metrics | grep -E "^(# TYPE|# UNIT)"
```
