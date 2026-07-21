---
title: "[Solution] Prometheus Query Too Expensive Error"
description: "How to fix Prometheus query too many samples or resources consumed"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Query scanning too many time series
- High cardinality metrics being queried
- `max_samples` limit exceeded
- Query touching too many blocks

## How to Fix

Increase max samples limit:

```yaml
global:
  query_max_samples: 500000
```

Optimize queries to reduce data scanned:

```promql
# Wrong: no label filter
rate(http_requests_total[5m])

# Better: filter to specific jobs
rate(http_requests_total{job="my-app"}[5m])

# Even better: use recording rules
job:http_requests:rate5m
```

## Examples

```bash
# Check sample count
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_engine_query_samples_total'

# Find high-cardinality metrics
curl -s http://localhost:9090/api/v1/status/tsdb | jq '.data.seriesCountByMetricName[:10]'

# Test query cost
curl -s -w '
%{time_total}' 'http://localhost:9090/api/v1/query?query=http_requests_total'
```
