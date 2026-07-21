---
title: "[Solution] Prometheus Metrics Path Error"
description: "How to fix Prometheus metrics endpoint path configuration errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- `metrics_path` not set when target uses a non-default path
- Default path `/metrics` not exposed by the application
- Typo in the configured metrics path
- Application uses a different endpoint for metrics

## How to Fix

Set the correct metrics path in scrape config:

```yaml
scrape_configs:
  - job_name: 'app'
    metrics_path: '/custom/metrics'
    static_configs:
      - targets: ['localhost:8080']
```

Verify the metrics endpoint exists:

```bash
curl -s http://target-host:8080/metrics | head -5
curl -s http://target-host:8080/custom/metrics | head -5
```

Check available endpoints:

```bash
curl -s http://target-host:8080/ | grep -i metric
```

Common alternative paths:

```yaml
# Spring Boot Actuator
metrics_path: '/actuator/prometheus'

# Custom path
metrics_path: '/internal/metrics'

# Debug endpoint
metrics_path: '/debug/vars'
```

## Examples

```bash
# Test different metrics paths
curl -s http://localhost:8080/metrics
curl -s http://localhost:8080/actuator/prometheus
curl -s http://localhost:8080/debug/metrics

# Check scrape config
promtool check config prometheus.yml
```
