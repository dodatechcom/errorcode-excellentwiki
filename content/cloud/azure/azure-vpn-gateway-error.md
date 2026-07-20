---
title: "[Solution] Azure VPN Gateway Error — tunnel, connection, and policy failures"
description: "Fix Azure VPN Gateway error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 106
---

VPN Gateway errors appear as failed tunnel establishments, disconnections, or phase 1/phase 2 SA negotiation failures between on-premises and Azure.

## Common Causes
- IKE/IPsec policy mismatch between local and Azure VPN gateways
- Pre-shared key (PSK) mismatch on connection resources
- Route table not advertising VNet address spaces through gateway
- Public IP address changes breaking existing tunnel configurations
- Gateway SKU insufficient for required throughput

## How to Fix
### Check VPN gateway connection status
```bash
az network vnet-gateway list-connections \
  --resource-group myResourceGroup \
  --name myVnetGateway \
  --query "[].{name:name, connectionStatus:connectionStatus, ingressBytesTransferred:ingressBytesTransferred}"
```

### Update connection PSK
```bash
az network vpn-connection update \
  --resource-group myResourceGroup \
  --name myVpnConnection \
  --shared-key "NewPreSharedKey123!"
```

### Set IPsec policy
```bash
az network vpn-connection ipsec-policy set \
  --resource-group myResourceGroup \
  --connection-name myVpnConnection \
  --dh-group DHGroup14 \
  --ike-encryption AES256 \
  --ike-integrity SHA256 \
  --ipsec-encryption AES256 \
  --ipsec-integrity SHA256 \
  --pfs-group PFS14 \
  --sa-lifetime 3600 \
  --sa-datasize 1024
```

### Verify route propagation
```bash
az network vnet-gateway list-route-tables \
  --resource-group myResourceGroup \
  --name myVnetGateway
```

## Examples
### Create new VPN connection
```bash
az network vpn-connection create \
  --resource-group myResourceGroup \
  --name myVpnConnection \
  --vnet-gateway1 myVnetGateway \
  --shared-key "MySharedKey123!" \
  --enable-bgp false
```

### Check gateway effective routes
```bash
az network vnet-gateway show-effective-route-table \
  --resource-group myResourceGroup \
  --name myVnetGateway
```

## Related Errors
- {{< relref "/cloud/azure/azure-vnet-error" >}}
- {{< relref "/cloud/azure/azure-expressroute-error" >}}
- {{< relref "/cloud/azure/azure-route-table-error" >}}
