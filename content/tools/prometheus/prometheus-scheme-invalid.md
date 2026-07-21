---
title: "[Solution] Prometheus Scrape Scheme Invalid"
description: "How to fix invalid scheme configuration in Prometheus scrape targets"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- `scheme` value is not `http` or `https`
- Typo in scheme field (e.g., `htps`, `httpss`)
- Using `https` without proper TLS configuration
- Scheme does not match the target endpoint

## How to Fix

Set valid scheme value:

```yaml
scrape_configs:
  - job_name: 'app'
    scheme: 'https'
    static_configs:
      - targets: ['localhost:8443']
```

Valid scheme values:

```yaml
scheme: 'http'   # default
scheme: 'https'
```

Verify target supports the scheme:

```bash
curl -k https://localhost:8443/metrics
curl http://localhost:8080/metrics
```

## Examples

```bash
# Test HTTP scheme
curl http://localhost:9090/metrics

# Test HTTPS scheme
curl -k https://localhost:9443/metrics

# Validate config
promtool check config prometheus.yml
```
