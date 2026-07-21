---
title: "[Solution] Prometheus DigitalOcean Service Discovery Error"
description: "How to fix Prometheus DigitalOcean-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid API token
- Rate limiting from DigitalOcean API
- Droplet not tagged properly
- Network blocking scrape port

## How to Fix

Configure DigitalOcean SD:

```yaml
scrape_configs:
  - job_name: 'digitalocean'
    digitalocean_sd_configs:
      - access_token: your-api-token
        port: 9100
```

## Examples

```bash
# Test API token
curl -X GET -H "Authorization: Bearer YOUR_TOKEN" "https://api.digitalocean.com/v2/account"

# List droplets
curl -X GET -H "Authorization: Bearer YOUR_TOKEN" "https://api.digitalocean.com/v2/droplets"

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_digitalocean != null)'
```
