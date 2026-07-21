---
title: "[Solution] Prometheus Query Tail Error"
description: "How to fix Prometheus query tail (last values) errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Query returning no data for requested time range
- Step too large for data resolution
- Metric does not exist at query time
- Stale data markers causing gaps

## How to Fix

Adjust query step size:

```promql
# Better resolution with smaller step
http_requests_total[5m] offset 5m

# Check current step
curl -s 'http://localhost:9090/api/v1/query?query=http_requests_total&time=now'
```

Use `last_over_time` for current values:

```promql
last_over_time(http_requests_total[1h])
```

## Examples

```bash
# Get latest value
curl -s 'http://localhost:9090/api/v1/query?query=last_over_time(http_requests_total[5m])'

# Check data availability
curl -s 'http://localhost:9090/api/v1/query_range?query=http_requests_total&start=1h ago&end=now&step=60s' | jq '.data.result | length'
```
