---
title: "[Solution] Prometheus Histogram Bucket Error"
description: "How to fix histogram bucket errors in Prometheus metrics"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Bucket boundaries not monotonically increasing
- Missing `_count` or `_sum` for histogram
- Bucket values not cumulative
- Custom bucket boundaries overlapping

## How to Fix

Define proper histogram buckets:

```python
from prometheus_client import Histogram

# Custom buckets must be monotonically increasing
HISTOGRAM = Histogram(
    'request_duration_seconds',
    'Request duration',
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]
)
```

Use default buckets for standard metrics:

```python
# Default buckets: (.005, .01, .025, .05, .1, .25, .5, 1, 2.5, 5, 10)
HISTOGRAM = Histogram('request_duration_seconds', 'Request duration')
```

Verify histogram output:

```bash
curl -s http://target:8080/metrics | grep "request_duration_seconds_bucket"
```

## Examples

```bash
# Query histogram quantiles
curl -s 'http://localhost:9090/api/v1/query?query=histogram_quantile(0.99,rate(request_duration_seconds_bucket[5m]))'

# View raw histogram buckets
curl -s http://target:8080/metrics | grep "request_duration_seconds_bucket"
```
