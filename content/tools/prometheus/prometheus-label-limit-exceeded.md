---
title: "[Solution] Prometheus Label Limit Exceeded"
description: "How to fix Prometheus label limit exceeded errors during ingestion"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Target exporting metrics with too many labels
- Label cardinality too high causing memory pressure
- Default label limit reached per sample
- High-cardinality labels like user_id or request_id

## How to Fix

Increase the label limit:

```yaml
global:
  label_limit: 50
```

Per-scrape label limit:

```yaml
scrape_configs:
  - job_name: 'high-cardinality-app'
    label_limit: 100
    label_name_length_limit: 200
    label_value_length_limit: 4000
```

Reduce label cardinality on the target:

```python
# Bad: high cardinality label
REQUEST_COUNT.labels(url="/api/user/{id}", method="GET", status="200")

# Better: low cardinality labels
REQUEST_COUNT.labels(endpoint="/api/user", method="GET", status="200")
```

## Examples

```bash
# Check label count per metric
curl -s 'http://localhost:9090/api/v1/label/__name__/values' | jq length

# Monitor label usage
promtool tsdb analyze prometheus-data/ 2>&1 | grep label
```
