---
title: "[Solution] Prometheus Native Histogram Error"
description: "How to fix native histogram errors in Prometheus"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Schema version not supported by Prometheus
- Bucket count mismatch with schema
- Native histogram not enabled in configuration
- Incompatible client library version

## How to Fix

Enable native histograms:

```yaml
storage:
  tsdb:
    enable_native_histograms: true
```

Use compatible client library:

```python
from prometheus_client import Histogram

# Native histogram with custom schema
HISTOGRAM = Histogram(
    'request_duration_seconds',
    'Request duration',
    buckets=[0.01, 0.1, 1, 10]
)
```

Query native histograms:

```promql
histogram_quantile(0.99, request_duration_seconds_bucket)
```

## Examples

```bash
# Check native histogram support
promtool version

# Query histogram bucket distribution
curl -s 'http://localhost:9090/api/v1/query?query=request_duration_seconds_bucket'

# Enable native histograms in config
prometheus --enable-feature=native-histograms
```
