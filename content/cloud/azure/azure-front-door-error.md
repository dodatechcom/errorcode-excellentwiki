---
title: "[Solution] Azure Front Door Error — WAF, backend pool, and routing failures"
description: "Fix Azure Front Door error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 101
---

Azure Front Door errors occur when WAF rules block legitimate traffic, backend health probes fail, or routing rules misconfigure. These issues cause 502/503 errors and latency spikes.

## Common Causes
- WAF policy blocking valid requests with overly restrictive rules
- Backend health probes timing out or returning non-200 status codes
- Origin group misconfiguration with incorrect priority or weight settings
- SSL certificate expiration or mismatch on custom domains
- Routing rules pointing to non-existent or unhealthy backends

## How to Fix
### Check backend health
```bash
az network front-door backend-health show \
  --resource-group myResourceGroup \
  --front-door-name myFrontDoor \
  --name myBackendPool
```

### Update WAF policy to allow traffic
```bash
az network front-door waf-policy rule create \
  --policy-name myWafPolicy \
  --resource-group myResourceGroup \
  --name AllowLegitimateTraffic \
  --rule-type Override \
  --action Allow \
  --priority 100
```

### Verify origin group health probe settings
```bash
az network front-door origin-group update \
  --resource-group myResourceGroup \
  --front-door-name myFrontDoor \
  --name myOriginGroup \
  --probe-path "/health" \
  --probe-interval 30
```

### Reconfigure routing rule
```bash
az network front-door routing-rule update \
  --resource-group myResourceGroup \
  --front-door-name myFrontDoor \
  --name myRoutingRule \
  --frontend-endpoints myFrontendEndpoint \
  --backend-pool-name myBackendPool
```

## Examples
### Fix 502 error from unhealthy backend
```bash
az network front-door backend update \
  --resource-group myResourceGroup \
  --front-door-name myFrontDoor \
  --backend-pool-name myBackendPool \
  --name myBackend \
  --address myapp.azurewebsites.net \
  --priority 1 \
  --http-port 80 \
  --https-port 443
```

### Enable WAF in prevention mode
```bash
az network front-door waf-policy policy-settings update \
  --policy-name myWafPolicy \
  --resource-group myResourceGroup \
  --mode Prevention \
  --state Enabled
```

## Related Errors
- {{< relref "/cloud/azure/azure-cdn-error" >}}
- {{< relref "/cloud/azure/azure-firewall-error" >}}
- {{< relref "/cloud/azure/azure-dns-error" >}}
