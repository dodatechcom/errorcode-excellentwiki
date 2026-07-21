---
title: "[Solution] Prometheus HTTP Client Error"
description: "How to fix Prometheus HTTP client errors when connecting to targets"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- TLS certificate verification failure
- Connection refused by target
- HTTP redirect loop
- DNS resolution failure
- Connection timeout

## How to Fix

Configure HTTP client settings:

```yaml
scrape_configs:
  - job_name: 'app'
    http_client_config:
      tls_config:
        insecure_skip_verify: true  # For testing only
      follow_redirects: true
      proxy_url: 'http://proxy:8080'
```

Check target connectivity:

```bash
curl -v http://target-host:8080/metrics
```

## Examples

```bash
# Test HTTP connection
curl -v http://target:8080/metrics

# Check with proxy
curl -x http://proxy:8080 http://target:8080/metrics

# View client errors
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_target_sync_length'
```
