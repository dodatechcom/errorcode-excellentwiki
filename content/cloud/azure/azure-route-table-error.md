---
title: "[Solution] Azure Route Table Error — route, effective route, and propagation failures"
description: "Fix Azure Route Table error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 110
---

Route table errors occur when static routes conflict with BGP propagation, next-hop appliances become unreachable, or subnet associations misroute traffic.

## Common Causes
- Static route overriding BGP-learned routes with incorrect next-hop
- Next-hop appliance IP address no longer reachable
- Route table not associated with the correct subnet
- BGP route propagation disabled on gateway subnet
- Overlapping route prefixes causing longest-match ambiguity

## How to Fix
### Check effective routes on subnet
```bash
az network vnet-gateway show-effective-route-table \
  --resource-group myResourceGroup \
  --name myVnetGateway
```

### Update route next-hop
```bash
az network route-table route update \
  --resource-group myResourceGroup \
  --route-table-name myRouteTable \
  --name myRoute \
  --address-prefix 10.1.0.0/16 \
  --next-hop-type VirtualAppliance \
  --next-hop-ip-address 10.0.0.4
```

### Disable route propagation on gateway
```bash
az network route-table update \
  --resource-group myResourceGroup \
  --name myRouteTable \
  --disable-bgp-route-propagation
```

### Associate route table with subnet
```bash
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name mySubnet \
  --route-table myRouteTable
```

## Examples
### Create route table with UDR
```bash
az network route-table create \
  --resource-group myResourceGroup \
  --name myUDRTable \
  --location eastus
```

### List all routes in table
```bash
az network route-table route list \
  --resource-group myResourceGroup \
  --route-table-name myUDRTable \
  --output table
```

## Related Errors
- {{< relref "/cloud/azure/azure-vnet-error" >}}
- {{< relref "/cloud/azure/nsg-error" >}}
- {{< relref "/cloud/azure/azure-firewall-error" >}}
