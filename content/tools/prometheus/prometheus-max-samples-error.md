---
title: "[Solution] Prometheus Max Samples Limit Error"
description: "How to fix Prometheus maximum samples exceeded during query"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Query result contains more than `max_samples` data points
- High cardinality metrics returning many series
- Large time range queried with small step
- Recording rules generating excessive samples

## How to Fix

Increase sample limit:

```yaml
global:
  query_max_samples: 1000000
```

Optimize query to reduce samples:

```promql
# Wrong: high cardinality
sum(rate(http_requests_total[5m]))

# Better: aggregate with labels
sum(rate(http_requests_total{job="app"}[5m])) by (status)
```

## Examples

```bash
# Check sample limit
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.queryMaxSamples'

# Count series
curl -s 'http://localhost:9090/api/v1/query?query=count({__name__!=""})'
```
