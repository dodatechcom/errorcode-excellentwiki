---
title: "[Solution] Prometheus Hetzner Service Discovery Error"
description: "How to fix Prometheus Hetzner-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid Hetzner Cloud API token
- Server not accessible from Prometheus
- Wrong API endpoint
- Firewall blocking scrape port

## How to Fix

Configure Hetzner SD:

```yaml
scrape_configs:
  - job_name: 'hetzner'
    hetzner_sd_configs:
      - role: robot
        port: 9100
```

## Examples

```bash
# Test Hetzner API
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.hetzner.cloud/v1/servers

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_hetzner != null)'
```
