---
title: "[Solution] Prometheus Consul Service Discovery Error"
description: "How to fix Prometheus Consul-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Consul agent unreachable
- Wrong Consul datacenter specified
- ACL token insufficient permissions
- Consul services not registered properly

## How to Fix

Configure Consul SD:

```yaml
scrape_configs:
  - job_name: 'consul'
    consul_sd_configs:
      - server: 'consul.example.com:8500'
        services: []
        tags: ['prometheus']
        token: 'your-consul-acl-token'
```

## Examples

```bash
# Test Consul connectivity
curl http://consul:8500/v1/agent/self

# List registered services
curl http://consul:8500/v1/catalog/services

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_consul_service != null)'
```
