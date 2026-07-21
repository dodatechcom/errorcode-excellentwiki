---
title: "[Solution] Prometheus Max Concurrency Exceeded Error"
description: "How to fix Prometheus maximum concurrent query limit exceeded"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Too many concurrent queries running
- `query.max-concurrency` too low
- Dashboard queries all executing simultaneously
- Heavy recording rules running in parallel

## How to Fix

Increase max concurrency:

```yaml
global:
  query_max_concurrency: 20
```

Monitor concurrent queries:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_engine_queries_concurrent'
```

Check current limit:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.queryConcurrency'
```

## Examples

```bash
# Check concurrent queries
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_engine_queries_concurrent'

# View query stats
curl -s http://localhost:9090/api/v1/status/stats | jq '.data.query'
```
