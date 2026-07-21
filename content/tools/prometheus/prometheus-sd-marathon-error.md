---
title: "[Solution] Prometheus Marathon Service Discovery Error"
description: "How to fix Prometheus Marathon-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Marathon API unreachable
- Wrong Marathon endpoint URL
- Application not exposing metrics port
- Health check failing for Marathon apps

## How to Fix

Configure Marathon SD:

```yaml
scrape_configs:
  - job_name: 'marathon'
    marathon_sd_configs:
      - servers:
          - 'http://marathon.example.com:8080'
        groups:
          - 'production'
```

## Examples

```bash
# Test Marathon API
curl http://marathon.example.com:8080/v2/info

# List applications
curl http://marathon.example.com:8080/v2/apps

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_marathon_app != null)'
```
