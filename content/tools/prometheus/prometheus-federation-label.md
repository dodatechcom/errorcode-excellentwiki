---
title: "[Solution] Prometheus Federation Label Error"
description: "How to fix label handling errors in Prometheus federation"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Label conflicts between federated and local metrics
- `honor_labels` not set causing label overwrite
- Federated labels missing required values
- Label duplication across federation targets

## How to Fix

Use `honor_labels` for federation:

```yaml
scrape_configs:
  - job_name: 'federate'
    honor_labels: true
    metrics_path: '/federate'
    params:
      'match[]':
        - '{__name__=~".+"}'
    static_configs:
      - targets:
          - 'upstream:9090'
```

## Examples

```bash
# Check label conflicts
curl -s 'http://localhost:9090/api/v1/query?query=up' | jq '.data.result[].metric'

# Verify honor_labels setting
curl -s http://localhost:9090/api/v1/status/config | grep honor_labels
```
