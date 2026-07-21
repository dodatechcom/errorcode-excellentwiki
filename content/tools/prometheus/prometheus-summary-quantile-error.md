---
title: "[Solution] Prometheus Summary Quantile Error"
description: "How to fix summary quantile calculation errors in Prometheus"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Quantile values showing NaN (insufficient data)
- Error margin too high in quantile estimation
- Summary not receiving new observations
- Moving average window too narrow

## How to Fix

Configure summary quantiles properly:

```python
from prometheus_client import Summary

SUMMARY = Summary(
    'request_duration_seconds',
    'Request duration',
    ['method'],
    quantiles={0.5: 0.05, 0.9: 0.01, 0.99: 0.001}
)
```

Check if summary is receiving observations:

```bash
curl -s http://target:8080/metrics | grep "request_duration_seconds_count"
```

Use histograms for better accuracy:

```python
from prometheus_client import Histogram

# Histogram allows server-side quantile calculation
HISTOGRAM = Histogram('request_duration_seconds', 'Request duration')
```

## Examples

```bash
# Query summary quantile
curl -s 'http://localhost:9090/api/v1/query?query=request_duration_seconds{quantile="0.99"}'

# Compare with histogram quantile
curl -s 'http://localhost:9090/api/v1/query?query=histogram_quantile(0.99,rate(request_duration_seconds_bucket[5m]))'
```
