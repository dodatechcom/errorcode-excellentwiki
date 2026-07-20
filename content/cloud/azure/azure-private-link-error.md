---
title: "[Solution] Azure Private Link Error — endpoint, zone, and DNS failures"
description: "Fix Azure Private Link error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 109
---

Private Link errors manifest as connection failures, DNS resolution mismatches, or private endpoint IP conflicts that block access to PaaS services.

## Common Causes
- Private endpoint IP address overlapping with existing subnet ranges
- DNS zone not linked to VNet for private endpoint resolution
- Service provider rejecting connection approval
- Network security group blocking traffic to private endpoint IPs
- Private DNS zone virtual network links missing

## How to Fix
### Check private endpoint connection state
```bash
az network private-endpoint list \
  --resource-group myResourceGroup \
  --query "[].{name:name, connectionStatus:privateLinkServiceConnections[].status}"
```

### Create private DNS zone link
```bash
az network private-dns zone vnet-link create \
  --resource-group myResourceGroup \
  --zone-name privatelink.database.windows.net \
  --name myDnsLink \
  --virtual-network myVNet
```

### Approve pending connection
```bash
az network private-endpoint connection approve \
  --resource-group myResourceGroup \
  --name myPrivateEndpointConnection \
  --private-link-resource-id /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Storage/storageAccounts/myStorage \
  --description "Approved"
```

### Add NSG rule for private endpoint traffic
```bash
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name mySubnetNSG \
  --name AllowPrivateEndpoint \
  --priority 200 \
  --destination-address-prefixes 10.0.2.0/24 \
  --access Allow \
  --protocol Tcp \
  --direction Inbound
```

## Examples
### Create private endpoint for Storage
```bash
az network private-endpoint create \
  --resource-group myResourceGroup \
  --name myStoragePrivateEndpoint \
  --vnet-name myVNet \
  --subnet myPrivateEndpointSubnet \
  --private-connection-resource-id /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Storage/storageAccounts/myStorage \
  --group-id blob \
  --connection-name myBlobConnection
```

### Check private endpoint DNS configuration
```bash
az network private-endpoint show \
  --resource-group myResourceGroup \
  --name myPrivateEndpoint \
  --query "customDnsConfigs"
```

## Related Errors
- {{< relref "/cloud/azure/azure-dns-error" >}}
- {{< relref "/cloud/azure/azure-vnet-error" >}}
- {{< relref "/cloud/azure/nsg-error" >}}
