---
title: "[Solution] Prometheus Azure Service Discovery Error"
description: "How to fix Prometheus Azure-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Azure credentials misconfigured
- Wrong subscription or resource group
- VM not properly tagged
- Network security group blocking port

## How to Fix

Configure Azure SD:

```yaml
scrape_configs:
  - job_name: 'azure'
    azure_sd_configs:
      - subscription_id: your-subscription-id
        resource_group: your-resource-group
        port: 80
```

## Examples

```bash
# Test Azure credentials
az login
az account show

# List VMs
az vm list --resource-group your-rg --output table

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_azure_vm != null)'
```
