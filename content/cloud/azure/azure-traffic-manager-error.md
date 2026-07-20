---
title: "[Solution] Azure Traffic Manager Error — endpoint, profile, and routing failures"
description: "Fix Azure Traffic Manager error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 104
---

Traffic Manager errors occur when endpoints become disabled, health checks fail, or DNS routing misconfigurations cause traffic to route incorrectly.

## Common Causes
- Endpoint marked as disabled or stopped due to health check failures
- DNS TTL too high causing stale records during failover
- Routing method not suitable for the application topology
- Endpoint monitor path returning non-healthy status
- Profile DNS name conflicts or CNAME misconfiguration

## How to Fix
### Check endpoint health status
```bash
az network traffic-manager endpoint list \
  --resource-group myResourceGroup \
  --profile-name myTmProfile \
  --query "[].{name:name, status:endpointStatus, health:monitorStatus}"
```

### Enable endpoint and reset health
```bash
az network traffic-manager endpoint update \
  --resource-group myResourceGroup \
  --profile-name myTmProfile \
  --name myEndpoint \
  --type azureEndpoints \
  --endpoint-status Enabled
```

### Update profile DNS TTL
```bash
az network traffic-manager profile update \
  --resource-group myResourceGroup \
  --name myTmProfile \
  --unique-dns-name mytm.uniquedns.com \
  --ttl 30
```

### Change routing method
```bash
az network traffic-manager profile update \
  --resource-group myResourceGroup \
  --name myTmProfile \
  --routing-method Priority
```

## Examples
### Create failover endpoint
```bash
az network traffic-manager endpoint create \
  --resource-group myResourceGroup \
  --profile-name myTmProfile \
  --name primaryEndpoint \
  --type azureEndpoints \
  --target myapp-primary.azurewebsites.net \
  --endpoint-status Enabled
```

### Test DNS resolution
```bash
nslookup mytm.uniquedns.com
```

## Related Errors
- {{< relref "/cloud/azure/azure-dns-error" >}}
- {{< relref "/cloud/azure/azure-front-door-error" >}}
- {{< relref "/cloud/azure/azure-cdn-error" >}}
