---
title: "[Solution] Azure ExpressRoute Error — circuit, peering, and BGP failures"
description: "Fix Azure ExpressRoute error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 105
---

ExpressRoute errors involve circuit provisioning failures, peering configuration issues, or BGP route propagation problems that break connectivity to Azure.

## Common Causes
- Circuit not provisioned by connectivity provider
- BGP peering session not establishing due to ASN mismatch
- Route filter not applied or incorrect prefix advertisements
- Private peering not configured or VLAN ID conflicts
- ExpressRoute Global Reach circuit pairing failures

## How to Fix
### Check circuit provisioning state
```bash
az network express-route list \
  --resource-group myResourceGroup \
  --query "[].{name:name, circuitProvisioningState:circuitProvisioningState, serviceProviderProvisioningState:serviceProviderProvisioningState}"
```

### Enable private peering
```bash
az network express-route peering create \
  --resource-group myResourceGroup \
  --name myPrivatePeering \
  --express-route-name myCircuit \
  --peering-type AzurePrivatePeering \
  --peer-asn 100 \
  --primary-peer-address-prefix 10.0.0.0/30 \
  --secondary-peer-address-prefix 10.0.0.4/30 \
  --vlan-id 200
```

### Configure route filter for Microsoft peering
```bash
az network route-filter create \
  --resource-group myResourceGroup \
  --name myRouteFilter
```

### Verify BGP session status
```bash
az network express-route list \
  --resource-group myResourceGroup \
  --query "[].bgpPeeringProperties.{peerAsn:peerAsn, primaryCircuit:primaryCircuitAddressPrefix, secondaryCircuit:secondaryCircuitAddressPrefix}"
```

## Examples
### Create new ExpressRoute circuit
```bash
az network express-route create \
  --resource-group myResourceGroup \
  --name myCircuit \
  --bandwidth 200 \
  --peering-location "Washington DC" \
  --provider-name "Equinix" \
  --sku-tier Standard \
  --sku-family MeteredData
```

### Check circuit bandwidth usage
```bash
az network express-route get-stats \
  --resource-group myResourceGroup \
  --name myCircuit
```

## Related Errors
- {{< relref "/cloud/azure/azure-vnet-error" >}}
- {{< relref "/cloud/azure/azure-vpn-gateway-error" >}}
- {{< relref "/cloud/azure/azure-route-table-error" >}}
