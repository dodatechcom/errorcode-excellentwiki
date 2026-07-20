---
title: "[Solution] Azure Load Balancer Error — probe, backend pool, and SNAT failures"
description: "Fix Azure Load Balancer error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 103
---

Load Balancer errors manifest as failed health probes, unreachable backend VMs, or SNAT port exhaustion that prevents outbound connectivity.

## Common Causes
- Health probe failing due to backend VM service not responding on probe port
- Backend pool members marked unhealthy by probe failures
- SNAT port exhaustion from too many concurrent outbound connections
- Load balancing rules referencing non-existent frontend or backend pools
- NSG blocking health probe traffic from load balancer service tags

## How to Fix
### Check load balancer health probe status
```bash
az network lb list \
  --resource-group myResourceGroup \
  --query "[].{name:name, probes:probes[].{name:name, protocol:probeSettings.protocol, port:probeSettings.port}}"
```

### Update health probe configuration
```bash
az network lb probe update \
  --resource-group myResourceGroup \
  --lb-name myLoadBalancer \
  --name myHealthProbe \
  --protocol tcp \
  --port 80 \
  --interval 15 \
  --threshold 2
```

### Add NSG rule for health probes
```bash
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name myNSG \
  --name AllowHealthProbe \
  --priority 100 \
  --destination-port-ranges 80 443 \
  --access Allow \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefixes AzureLoadBalancer
```

### Increase frontend IP configuration limits
```bash
az network lb frontend-ip update \
  --resource-group myResourceGroup \
  --lb-name myLoadBalancer \
  --name myFrontendIP \
  --public-ip-address myPublicIP
```

## Examples
### Create new load balancing rule
```bash
az network lb rule create \
  --resource-group myResourceGroup \
  --lb-name myLoadBalancer \
  --name myLbRule \
  --protocol Tcp \
  --frontend-port 80 \
  --backend-port 80 \
  --frontend-ip-name myFrontendIP \
  --backend-pool-name myBackendPool \
  --probe-name myHealthProbe
```

### Check SNAT port usage
```bash
az network lb list \
  --resource-group myResourceGroup \
  --query "[].outboundRules[].{name:name, allocatedPorts:allocatedOutboundPorts}"
```

## Related Errors
- {{< relref "/cloud/azure/azure-vnet-error" >}}
- {{< relref "/cloud/azure/nsg-error" >}}
- {{< relref "/cloud/azure/azure-vm-error" >}}
