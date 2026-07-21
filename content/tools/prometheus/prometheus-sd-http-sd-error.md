---
title: "[Solution] Prometheus HTTP Service Discovery Error"
description: "How to fix Prometheus HTTP-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- HTTP endpoint unreachable
- Invalid JSON response format
- Authentication required but not provided
- Response too large causing timeout

## How to Fix

Configure HTTP SD:

```yaml
scrape_configs:
  - job_name: 'http-sd'
    http_sd_configs:
      - url: 'http://discovery-service:8080/targets'
        refresh_interval: 5m
```

Expected JSON format:

```json
[
  {
    "targets": ["host1:8080"],
    "labels": {
      "__meta_custom_label": "value"
    }
  }
]
```

## Examples

```bash
# Test HTTP SD endpoint
curl http://discovery-service:8080/targets | python3 -m json.tool

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_custom_label != null)'
```
