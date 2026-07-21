---
title: "[Solution] Prometheus Linode Service Discovery Error"
description: "How to fix Prometheus Linode-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid Linode API token
- Linode API rate limiting
- Linode not tagged properly
- Network configuration blocking ports

## How to Fix

Configure Linode SD:

```yaml
scrape_configs:
  - job_name: 'linode'
    linode_sd_configs:
      - access_token: your-linode-api-token
        port: 9100
```

## Examples

```bash
# Test Linode API token
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.linode.com/v4/linode/instances

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_linode != null)'
```
