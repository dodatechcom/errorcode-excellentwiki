---
title: "[Solution] Prometheus Query Timeout Error"
description: "How to fix Prometheus query timeout errors during PromQL execution"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Query too complex or scanning too much data
- Query time range too large
- `query.timeout` set too low
- Server under heavy query load

## How to Fix

Increase query timeout:

```yaml
global:
  query_timeout: 2m
```

Optimize queries:

```promql
# Wrong: scanning 30 days
rate(http_requests_total[30d])

# Better: use recording rules
# Pre-compute in recording rule
```

Check query performance:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.queryTimeout'
```

## Examples

```bash
# Test query timeout
curl -s --max-time 30 'http://localhost:9090/api/v1/query?query=rate(http_requests_total[1h])'

# Check query stats
curl -s http://localhost:9090/api/v1/status/stats | jq '.data.query'

# View slow queries
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_engine_query_duration_seconds'
```
