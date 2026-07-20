---
title: "[Solution] Azure Application Gateway Error — health probe, listener, and routing failures"
description: "Fix Azure Application Gateway error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 102
---

Application Gateway errors typically involve health probe failures, listener misconfigurations, or SSL certificate issues that cause backend pool members to become unhealthy.

## Common Causes
- Health probe path returning non-200 status from backend servers
- Listener port conflicts or SSL certificate binding failures
- Backend HTTP settings using incorrect protocol or port
- WAF policy blocking legitimate traffic
- Request routing rules not matching incoming requests

## How to Fix
### Check backend health status
```bash
az network application-gateway show-backend-health \
  --resource-group myResourceGroup \
  --name myAppGateway
```

### Update health probe configuration
```bash
az network application-gateway probe update \
  --resource-group myResourceGroup \
  --gateway-name myAppGateway \
  --name myHealthProbe \
  --path "/health" \
  --interval 30 \
  --timeout 10 \
  --threshold 3
```

### Fix listener SSL certificate
```bash
az network application-gateway ssl-cert create \
  --resource-group myResourceGroup \
  --gateway-name myAppGateway \
  --name mySslCert \
  --cert-file certificate.pfx \
  --cert-password CertPassword123
```

### Update backend HTTP settings
```bash
az network application-gateway http-settings update \
  --resource-group myResourceGroup \
  --gateway-name myAppGateway \
  --name myHttpSettings \
  --port 443 \
  --protocol Https \
  --cookie-based affinity Enabled
```

## Examples
### Add new backend server to pool
```bash
az network application-gateway address-pool address add \
  --resource-group myResourceGroup \
  --gateway-name myAppGateway \
  --pool-name myAddressPool \
  --ip-address 10.0.1.10
```

### Reset WAF policy to detection mode
```bash
az network application-gateway waf-config set \
  --resource-group myResourceGroup \
  --gateway-name myAppGateway \
  --enabled true \
  --firewall-mode Detection \
  --rule-set-type OWASP \
  --rule-set-version 3.2
```

## Related Errors
- {{< relref "/cloud/azure/azure-front-door-error" >}}
- {{< relref "/cloud/azure/nsg-error" >}}
- {{< relref "/cloud/azure/azure-vnet-error" >}}
