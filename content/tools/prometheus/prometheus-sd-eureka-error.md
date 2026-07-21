---
title: "[Solution] Prometheus Eureka Service Discovery Error"
description: "How to fix Prometheus Eureka-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Eureka server unreachable
- Application not registered in Eureka
- Wrong metadata keys for Prometheus
- Eureka REST API version mismatch

## How to Fix

Configure Eureka SD:

```yaml
scrape_configs:
  - job_name: 'eureka'
    eureka_sd_configs:
      - servers:
          - 'http://eureka.example.com:8761'
        refresh_interval: 30s
```

## Examples

```bash
# Test Eureka API
curl http://eureka:8761/eureka/apps

# Check registered apps
curl http://eureka:8761/eureka/apps -H "Accept: application/json"

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_eureka_app_name != null)'
```
