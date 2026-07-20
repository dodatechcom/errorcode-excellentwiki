---
title: "[Solution] Azure Virtual WAN Error — hub, connection, and routing failures"
description: "Fix Azure Virtual WAN error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 107
---

Virtual WAN errors occur when hub connections fail, spoke VNet associations break, or routing intents create conflicts that prevent traffic flow between branches.

## Common Causes
- Hub VNet peering not established or in disconnected state
- VPN/ExpressRoute connection in hub failing due to credential issues
- Routing intent conflicting with static routes on spoke VNets
- Hub firewall policy blocking inter-hub traffic
- Virtual hub capacity exceeded during peak traffic

## How to Fix
### Check hub connection status
```bash
az network vhub connection list \
  --resource-group myResourceGroup \
  --vhub-name myVirtualHub \
  --query "[].{name:name, connectionStatus:connectionStatus, routingVnet:routingVnet.id}"
```

### Update hub connection routing
```bash
az network vhub connection update \
  --resource-group myResourceGroup \
  --vhub-name myVirtualHub \
  --name mySpokeConnection \
  --routing-associated-route-table "10.0.0.0/16,172.16.0.0/16"
```

### Create new VNet connection to hub
```bash
az network vhub connection create \
  --resource-group myResourceGroup \
  --vhub-name myVirtualHub \
  --name myNewSpoke \
  --remote-vnet /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Network/virtualNetworks/mySpokeVnet
```

### Set routing intent
```bash
az network vhub routing-intent create \
  --resource-group myResourceGroup \
  --vhub-name myVirtualHub \
  --routing-policy myPolicy \
  --destination-addresses "10.0.0.0/8,172.16.0.0/12" \
  --next-hop /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Network/azureFirewalls/myFirewall
```

## Examples
### Check Virtual WAN hub status
```bash
az network vwan hub list \
  --resource-group myResourceGroup \
  --query "[].{name:name, routingState:routingState, virtualHubRoutingState:virtualHubRoutingState}"
```

### List all connections in WAN
```bash
az network vhub connection list \
  --resource-group myResourceGroup \
  --vhub-name myVirtualHub \
  --output table
```

## Related Errors
- {{< relref "/cloud/azure/azure-vpn-gateway-error" >}}
- {{< relref "/cloud/azure/azure-expressroute-error" >}}
- {{< relref "/cloud/azure/azure-route-table-error" >}}
