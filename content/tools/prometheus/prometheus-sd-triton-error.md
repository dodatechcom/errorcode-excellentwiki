---
title: "[Solution] Prometheus Triton Service Discovery Error"
description: "How to fix Prometheus Triton-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Triton API unreachable
- Wrong datacenter specified
- Machine not provisioned with metrics port
- CloudAPI authentication failure

## How to Fix

Configure Triton SD:

```yaml
scrape_configs:
  - job_name: 'triton'
    triton_sd_configs:
      - endpoint: 'triton.example.com'
        account: 'your-account'
        dc: 'us-east-1'
        basic_auth:
          username: admin
          password: secret
```

## Examples

```bash
# Test Triton API
curl -k https://triton:8080/--cloudapi-/ping

# List instances
curl -k -u admin:secret https://triton:8080/--cloudapi-/machines

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_triton != null)'
```
