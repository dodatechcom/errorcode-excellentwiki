---
title: "[Solution] Prometheus Label Value Too Long"
description: "How to fix Prometheus label value length limit exceeded errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Label values exceeding the default 2048 character limit
- High-cardinality string labels
- Labels containing full URLs or paths
- Error messages used as label values

## How to Fix

Increase label value length limit:

```yaml
global:
  label_value_length_limit: 4096
```

Per-scrape configuration:

```yaml
scrape_configs:
  - job_name: 'app'
    label_value_length_limit: 8192
```

Reduce label value length in the application:

```python
# Bad: full URL as label value
REQUEST_COUNT.labels(url="/api/v1/users/1234567890/profile/settings")

# Better: sanitized label value
REQUEST_COUNT.labels(endpoint="/api/v1/users", operation="profile_settings")
```

## Examples

```bash
# Find long label values
curl -s http://target:8080/metrics | awk -F'=' '/\{.*=[^}]{200,}/' | head

# Check current limit
curl -s http://localhost:9090/api/v1/status/config | jq '.data.yaml'
```
