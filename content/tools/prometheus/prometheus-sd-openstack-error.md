---
title: "[Solution] Prometheus OpenStack Service Discovery Error"
description: "How to fix Prometheus OpenStack-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- OpenStack credentials invalid
- Wrong project/domain ID
- Nova API unreachable
- Security groups blocking scrape port

## How to Fix

Configure OpenStack SD:

```yaml
scrape_configs:
  - job_name: 'openstack'
    openstack_sd_configs:
      - role: instance
        identity_endpoint: https://identity.example.com/v3
        username: prometheus
        password: secret
        project_name: monitoring
        domain_name: Default
```

## Examples

```bash
# Test OpenStack credentials
openstack token issue

# List instances
openstack server list

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_openstack != null)'
```
