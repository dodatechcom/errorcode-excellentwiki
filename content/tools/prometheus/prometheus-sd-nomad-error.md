---
title: "[Solution] Prometheus Nomad Service Discovery Error"
description: "How to fix Prometheus Nomad-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Nomad API unreachable
- ACL token insufficient permissions
- Job not exposing metrics port
- Namespace filtering misconfigured

## How to Fix

Configure Nomad SD:

```yaml
scrape_configs:
  - job_name: 'nomad'
    nomad_sd_configs:
      - server: 'http://nomad.example.com:4646'
        token: 'your-nomad-acl-token'
        namespaces: ['production']
```

## Examples

```bash
# Test Nomad API
curl http://nomad:4646/v1/status/leader

# List jobs
curl -H "X-Nomad-Token: YOUR_TOKEN" http://nomad:4646/v1/jobs

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_nomad != null)'
```
